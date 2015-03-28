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
    rentalLineItem.date_due = '2015-05-05'
    rentalLineItem.date_out = '2015-04-01'
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

    lineitems = hmod.LineItem.objects.all().filter(product=None, return_line_item=None)

    params['lineitems'] = lineitems

    return templater.render_to_response(request, 'rental.manage.html', params)