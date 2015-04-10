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
from decimal import Decimal
from django.core.mail import send_mail
import datetime
import requests

templater = get_renderer('retail')


@view_function
# @permission_required('admin.agent_rights' , '/homepage/login')
def process_request(request):
    params = {}

    products = hmod.Product.objects.all().order_by('name')
    params['products'] = products

    return dmp_render_to_response(request, 'product.html', params)


@view_function
# @permission_required('admin.agent_rights', '/homepgage/login')
def checkout(request):
    params = {}

    cart = hmod.ShoppingCart.objects.get(user_id=request.user.id)
    lineitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, rental_line_item=None, return_line_item=None)
    rentalitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, product=None, return_line_item=None)
    returnitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, product=None, rental_line_item=None)
    address = hmod.Address.objects.get(user=request.user)

    producttotal = 0
    for lineitem in lineitems:
        productitemtotal = lineitem.product_price() * lineitem.quantity
        producttotal += productitemtotal

    rentaltotal = 0
    for rentalitem in rentalitems:
        rentalitemtotal = rentalitem.rental_item_price() * rentalitem.quantity
        rentaltotal += rentalitemtotal

    returntotal = 0
    for returnitem in returnitems:
        returnitemtotal = returnitem.return_line_item.rental_line_item.calc_returntotal()
        returntotal += returnitemtotal

    taxrate = Decimal(0.065)
    tax = round((rentaltotal + producttotal + returntotal) * taxrate, 2)
    total = round(rentaltotal + producttotal + returntotal + tax, 2)
    subtotal = round((total - tax), 2)

    params['lineitems'] = lineitems
    params['rentalitems'] = rentalitems
    params['returnitems'] = returnitems
    params['total'] = total
    params['tax'] = tax
    params['address'] = address
    params['subtotal'] = subtotal

    return dmp_render_to_response(request, 'checkout.review.html', params)


class PaymentForm(forms.Form):
    address = forms.CharField(required=True, max_length=50)
    city = forms.CharField(required=True, max_length=50)
    state = forms.CharField(required=True, max_length=50)
    zip = forms.CharField(required=True, max_length=50)
    name = forms.CharField(required=True, max_length=50)
    number = forms.CharField(required=True, max_length=50)
    exp_month = forms.CharField(required=True, max_length=50)
    exp_year = forms.CharField(required=True, max_length=50)
    cvc = forms.CharField(required=True, max_length=50)


@view_function
def payment(request):
    params = {}

    cart = hmod.ShoppingCart.objects.get(user_id=request.user.id)
    lineitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, rental_line_item=None, return_line_item=None)
    rentalitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, product=None, return_line_item=None)
    address = hmod.Address.objects.get(user=request.user)

    producttotal = 0
    for lineitem in lineitems:
        productitemtotal = lineitem.product_price() * lineitem.quantity
        producttotal += productitemtotal

    rentaltotal = 0
    for rentalitem in rentalitems:
        rentalitemtotal = rentalitem.rental_item_price() * rentalitem.quantity
        rentaltotal += rentalitemtotal

    taxrate = Decimal(0.065)
    tax = round((rentaltotal + producttotal) * taxrate, 2)
    total = round(rentaltotal + producttotal + tax, 2)
    subtotal = round((total - tax), 2)

    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = 'ffbe4a3ef6b5eb7099b271e312851d76'

    form = PaymentForm(initial={
        'address': address.address,
        'city': address.city,
        'state': address.state,
        'zip': address.zip,
        'name': '',
        'number': '',
        'exp_month': '',
        'exp_year': '',
        'cvc': '',
    })

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': total,
                'type': 'Visa',
                'number': form.cleaned_data['number'],
                'exp_month': form.cleaned_data['exp_month'],
                'exp_year': form.cleaned_data['exp_year'],
                'cvc': form.cleaned_data['cvc'],
                'name': form.cleaned_data['name'],
                'description': 'transaction',
            })

            print(r.text)
            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])
                raise forms.ValidationError(resp['error'])
            else:
                print(resp.keys())

            transaction = hmod.Transaction()
            transaction.date = datetime.datetime.now()
            transaction.total_cost = total
            transaction.user = request.user
            transaction.save()

            lineitems2 = hmod.LineItem.objects.all().filter(shopping_cart=cart)
            for lineitem in lineitems2:
                lineitem.shopping_cart = None
                lineitem.transaction = transaction
                lineitem.save()

            t = datetime.datetime.now()
            today = t.strftime('%a, %m/%d/%Y')

            params['resp'] = resp
            params['lineitems'] = lineitems
            params['rentalitems'] = rentalitems
            params['total'] = total
            params['tax'] = tax
            params['subtotal'] = subtotal
            params['address'] = address
            params['user'] = request.user
            params['today'] = today

            emailsubject = "Order placed on " + t.strftime('%m/%d/%Y %I:%M:%S %p')
            emailbody = dmp_render(request, 'order.confirmation.html', params)

            send_mail(emailsubject, emailbody, 'sterling@thecolonialheritage.me', [request.user.email],
                      html_message=emailbody, fail_silently=False)

            return dmp_render_to_response(request, 'checkout.confirmation.html', params)

    params['form'] = form

    return dmp_render_to_response(request, 'checkout.payment.html', params)