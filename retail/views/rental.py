__author__ = 'Sterling'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required, login_required
from .. import dmp_render_to_response, dmp_render
from django.core import management
import datetime
templater = get_renderer('retail')


@view_function
# @permission_required('admin.agent_rights' , '/homepage/login')
def process_request(request):
    params = {}

    rentableitems = hmod.RentableItem.objects.all().order_by('name')
    params['rentableitems'] = rentableitems

    return templater.render_to_response(request, 'rental.html', params)


@view_function
def create_rentalline_item(request):
    params = {}

    rid = request.urlparams[0]
    rentableitem = hmod.RentableItem.objects.get(id=rid)
    # wardrobeitem = ''

    rentalLineItem = hmod.RentalLineItem()
    rentalLineItem.date_due = '2015-02-05'
    rentalLineItem.date_out = '2015-02-01'
    rentalLineItem.discount_percent = 2.5
    rentalLineItem.rentable_item = rentableitem
    # rentalLineItem.wardrobe_item = wardrobeitem
    rentalLineItem.save()

    params['rlid'] = rentalLineItem
    # params['wardrobitem'] = wardrobeitem

    return HttpResponseRedirect('/retail/product.create_line_item/{}/1/rental'.format(rentalLineItem.id), params)


@view_function
# @permission_required('admin.agent_rights' , '/homepage/login')
def manage(request):
    params = {}

    lineitems = []
    rentalitems = hmod.RentalLineItem.objects.all().filter(returned=False)
    for rentalitem in rentalitems:
        try:
            lineitem = hmod.LineItem.objects.get(rental_line_item=rentalitem)
            lineitems.append(lineitem)
        except hmod.LineItem.DoesNotExist:
            pass

    params['lineitems'] = lineitems

    return templater.render_to_response(request, 'rental.manage.html', params)


@view_function
# @permission_required('admin.agent_rights', '/retail/login')
def delete_rental_item(request):

    try:
        lineitem = hmod.LineItem.objects.get(id=request.urlparams[0])
        rentalitem = hmod.RentalLineItem.objects.get(id=request.urlparams[0])
    except hmod.LineItem.DoesNotExist:
        return HttpResponseRedirect('/retail/product/')

    lineitem.delete()
    rentalitem.delete()

    return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')


@view_function
def return_lineitem(request):
    params = {}

    rid = request.urlparams[0]
    rentalitem = hmod.RentalLineItem.objects.get(id=rid)
    lineitem = hmod.LineItem.objects.get(rental_line_item=rentalitem)

    dayslate = rentalitem.calc_dayslate()
    subtotal = rentalitem.calc_subtotal()
    latefee = rentalitem.calc_latefee()
    tax = rentalitem.calc_tax()
    return_total = rentalitem.calc_returntotal()

    params['lineitem'] = lineitem
    params['dayslate'] = dayslate
    params['subtotal'] = subtotal
    params['latefee'] = latefee
    params['tax'] = tax
    params['return_total'] = return_total

    return templater.render_to_response(request, 'return_lineitem.html', params)


@view_function
def create_return_lineitem(request):
    params = {}

    rentalid = request.urlparams[0]
    rentalitem = hmod.RentalLineItem.objects.get(id=rentalid)
    now = datetime.datetime.now().date()

    returnLineItem = hmod.ReturnLineItem()
    returnLineItem.date_in = now
    # returnLineItem.damage_fee = params['damage_fee']
    returnLineItem.rental_line_item = rentalitem
    returnLineItem.days_late = returnLineItem.rental_line_item.calc_dayslate()
    returnLineItem.late_fee = returnLineItem.rental_line_item.calc_latefee()
    rentalitem.returned = True
    rentalitem.save()
    returnLineItem.save()

    subtotal = returnLineItem.rental_line_item.calc_subtotal()
    latefee = returnLineItem.rental_line_item.calc_latefee()
    tax = returnLineItem.rental_line_item.calc_tax()
    return_total = returnLineItem.rental_line_item.calc_returntotal()

    params['dayslate'] = returnLineItem.rental_line_item.calc_dayslate()
    params['subtotal'] = subtotal
    params['latefee'] = latefee
    params['tax'] = tax
    params['return_total'] = return_total

    return HttpResponseRedirect('/retail/product.create_line_item/{}/1/return'.format(returnLineItem.id), params)