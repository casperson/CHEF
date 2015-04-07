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
from django.core.mail import send_mail
import datetime
import decimal
import pprint

templater = get_renderer('retail')


@view_function
# @permission_required('admin.agent_rights' , '/homepage/login')
def process_request(request):
    params = {}

    products = hmod.Product.objects.all().order_by('name')
    params['products'] = products

    return dmp_render_to_response(request, 'product.html', params)


@view_function
# @permission_required('admin.agent_rights', '/retail/product')
def edit(request):
    params ={}

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/retail/product/')

    form = ProductEditForm(initial={
        'name': product.name,
        'description':product.description,
        'category': product.category,
        'price': product.price
    })

    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.save()
        return HttpResponseRedirect('/retail/product/')

    params['form'] = form
    params['retail'] = product

    return templater.render_to_response(request, 'product.edit.html', params)


class ProductEditForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=200, required=False)
    category = forms.CharField(max_length=20, required=True)
    price = forms.CharField(max_length=10, required=False)


@view_function
@permission_required('admin.agent_rights', '/retail/login')
def create(request):
    '''Create a new retail'''
    product = hmod.Product()
    product.name = ''
    product.description = ''
    product.category = ''
    product.current_price = 0.00
    product.save()

    return HttpResponseRedirect('/retail/product.edit/{}/'.format(product.id))


@view_function
# @permission_required('admin.agent_rights', '/retail/login')
def delete(request):

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/retail/product/')

    product.delete()

    return HttpResponseRedirect('/retail/product/')


@view_function
# @permission_required('admin.agent_rights', '/retail/login')
def delete_line_item(request):

    try:
        lineitem = hmod.LineItem.objects.get(id=request.urlparams[0])
    except hmod.LineItem.DoesNotExist:
        return HttpResponseRedirect('/retail/product/')

    lineitem.delete()

    return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    # return HttpResponseRedirect('retail/product.shoppingcart.html')


@view_function
# @permission_required('admin.agent_rights', '/homepage/login')
def detail(request):
    params = {}

    product = hmod.Product.objects.all().filter(id=request.urlparams[0])
    params['products'] = product

    return templater.render_to_response(request, 'product.detail.html', params)


@view_function
# @permission_required('admin.admin_rights', '/homepage/login/')
def create_line_item(request):
    params = {}

    pid = request.urlparams[0]
    qty = request.urlparams[1]
    decide = request.urlparams[2]

    lineItem = hmod.LineItem()
    cart = hmod.ShoppingCart.objects.get(user_id=request.user.id)
    lineItem.user = request.user

    if decide == 'rental':
        rentallineitem = hmod.RentalLineItem.objects.get(id=pid)
        lineItem.amount = rentallineitem.rentable_item.rental_price
        lineItem.quantity = qty
        lineItem.transaction = None
        lineItem.shopping_cart = cart
        lineItem.product = None
        lineItem.rental_line_item = rentallineitem
        lineItem.save()
    elif decide == 'product':
        product = hmod.Product.objects.get(id=pid)
        lineItem.amount = product.price
        lineItem.quantity = qty
        lineItem.transaction = None
        lineItem.shopping_cart = cart
        lineItem.product = product
        lineItem.rental_line_item = None
        lineItem.save()
    elif decide == 'return':
        returnLineItem = hmod.ReturnLineItem.objects.get(id=pid)
        lineItem.amount = returnLineItem.rental_line_item.rentable_item.rental_price
        lineItem.quantity = qty
        lineItem.transaction = None
        lineItem.shopping_cart = cart
        lineItem.product = None
        lineItem.rental_line_item = None
        lineItem.return_line_item = returnLineItem
        lineItem.save()

        return HttpResponse('/retail/rental.manage')

    params['pid'] = pid

    return HttpResponseRedirect('/retail/product.shopping_cart/', params)


@view_function
def shopping_cart(request):
    params = {}

    cart = hmod.ShoppingCart.objects.get(user_id=request.user.id)
    lineitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, rental_line_item=None, return_line_item=None)
    rentalitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, product=None, return_line_item=None)
    returnitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, product=None, rental_line_item=None)

    params['lineitems'] = lineitems
    params['rentalitems'] = rentalitems
    params['returnitems'] = returnitems

    return dmp_render_to_response(request, 'product.shoppingcart.html', params)


@view_function
def edit_line_item(request):
    params = {}

    # print(request.POST)
    # print(request)
    try:
        lineItem = hmod.LineItem.objects.get(id=request.urlparams[0])
        # product = hmod.Product.objects.get(id=request.urlparams[1])
    except hmod.Product.DoesNotExist:
        return HttpResponseRedirect('/retail/product/')

    # line_item = hmod.LineItem()
    # line_item.amount = amount
    # line_item.quantity = form.quantity
    # line_item.shopping_cart = shoppingCart.id
    # line_item.product = product.id

    form = LineItemEditForm(initial={
        'quantity': lineItem.quantity
    })

    if request.method == 'POST':
        form = LineItemEditForm(request.POST)
        form.lineitemid = lineItem.id
        if form.is_valid():
            lineItem.quantity = form.cleaned_data['quantity']

            lineItem.save()
            # return HttpResponseRedirect('/account/user/')
            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form
    params['lineItem'] = lineItem
    # params['product'] = product

    return dmp_render_to_response(request, 'product.edit_line_item.html', params)


class LineItemEditForm(forms.Form):
    quantity = forms.CharField(required=True, max_length=100)


@view_function
# @permission_required('admin.admin_rights', '/homepage/login/')
def search(request):
    params = {}

    search = hmod.Product.objects.filter(name__icontains=request.urlparams[0])

    params['search'] = search

    return templater.render_to_response(request, '/retail/product.search.html', params)


@view_function
def batch(request):
    params = {}
    # management.call_command('check_rentals', request)
    return dmp_render_to_response(request, 'check_rentals.html', params)


@view_function
def overduereport(request):
    params = {}

    rentals = hmod.RentalLineItem.objects.all()
    overdues = []
    thirty =[]
    sixty = []
    ninety =[]

    now = datetime.datetime.now().date()

    for rental in rentals:
        if rental.date_due < now:
            overdues.append(rental)
        else:
            pass

    for overdue in overdues:
        fee = None
        if overdue.rentable_item is not None:
            fee = hmod.RentableItem.objects.get(id=overdue.rentable_item.id)
        elif overdue.wardrobe_item is not None:
            fee = hmod.RentableItem.objects.get(id=overdue.wardrobe_item.id)

        item = hmod.LineItem.objects.get(rental_line_item=overdue)
        print(item)
        # shoppingcart = hmod.ShoppingCart.objects.get(user=item.shopping_cart)
        user = hmod.User.objects.get(id=item.shopping_cart.user_id)
        dayslatecalc = now - overdue.date_due
        dayslate = dayslatecalc.days.numerator

        overdueItem = {
            'id': item.id,
            'name': item.rental_item_name(),
            'datedue': overdue.date_due,
            'price': fee.price_per_day,
            'dayslate': dayslate,
            'latefee': fee.price_per_day * dayslate,
            'today': now,
            'renter': user.first_name + " " + user.last_name,
        }

        if 60 > dayslate > 29:
            thirty.append(overdueItem)
        elif 59 < dayslate < 90:
            sixty.append(overdueItem)
        elif dayslate > 89:
            ninety.append(overdueItem)

    params['thirty'] = thirty
    params['sixty'] = sixty
    params['ninety'] = ninety

    return dmp_render_to_response(request, 'overdue_report.html',params)