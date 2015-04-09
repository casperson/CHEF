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


@view_function
# @permission_required('admin.agent_rights', '/retail/product')
def edit(request):
    params = {}

    try:
        rentableitem = hmod.RentableItem.objects.get(id=request.urlparams[0])
    except hmod.RentableItem.DoesNotExist:
        return HttpResponseRedirect('/retail/rentalmanageitems/')

    form = RentableEditForm(initial={
        'Name': rentableitem.name,
        'Description': rentableitem.description,
        'Category': rentableitem.category.description,
        'Rental_Price': rentableitem.rental_price,
        'Price_Per_Day': rentableitem.price_per_day,
        'Value': rentableitem.value
    })

    if request.method == 'POST':

        form = RentableEditForm(request.POST)
        if form.is_valid():
            rentableitem.name = form.cleaned_data['Name']
            rentableitem.description = form.cleaned_data['Description']
            rentableitem.category = hmod.Category.objects.get(description=form.cleaned_data['Category'])
            rentableitem.rental_price = form.cleaned_data['Rental_Price']
            rentableitem.price_per_day = form.cleaned_data['Price_Per_Day']
            rentableitem.value = form.cleaned_data['Value']
            rentableitem.save()
        return HttpResponseRedirect('/retail/rental.manageitems/')

    params['form'] = form
    params['rentableitem'] = rentableitem

    return templater.render_to_response(request, 'rental.edititem.html', params)


class RentableEditForm(forms.Form):
    Name = forms.CharField(max_length=50, required=True, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Description = forms.CharField(max_length=200, required=False, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Category = forms.CharField(max_length=20, required=True, label='Category', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Rental_Price = forms.CharField(max_length=10, required=True, label='Rental Price', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Price_Per_Day = forms.CharField(max_length=10, required=True, label='Price Per Day', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Value = forms.CharField(max_length=10, required=True, label='Value', widget=forms.TextInput(attrs={'class': 'form-control'}))


@view_function
# @permission_required('admin.agent_rights', '/retail/product')
def editwardrobeitem(request):
    params = {}

    try:
        wardrobeitem = hmod.WardrobeItem.objects.get(id=request.urlparams[0])
    except hmod.WardrobeItem.DoesNotExist:
        return HttpResponseRedirect('/retail/rentalmanageitems/')

    form = WardrobeEditForm(initial={
        'Name': wardrobeitem.name,
        'Description': wardrobeitem.description,
        'Category': wardrobeitem.category.description,
        'Rental_Price': wardrobeitem.rental_price,
        'Price_Per_Day': wardrobeitem.price_per_day,
        'Value': wardrobeitem.value,
        'Gender': wardrobeitem.gender,
        'Color': wardrobeitem.color,
        'Pattern': wardrobeitem.pattern,
        'Size': wardrobeitem.size,
        'SizeModifier_': wardrobeitem.size_modifier,
        'Start_Year': wardrobeitem.start_year,
        'End_Year': wardrobeitem.end_year,
    })

    if request.method == 'POST':

        form = WardrobeEditForm(request.POST)
        if form.is_valid():
            wardrobeitem.name = form.cleaned_data['Name']
            wardrobeitem.description = form.cleaned_data['Description']
            wardrobeitem.category = hmod.Category.objects.get(description=form.cleaned_data['Category'])
            wardrobeitem.rental_price = form.cleaned_data['Rental_Price']
            wardrobeitem.price_per_day = form.cleaned_data['Price_Per_Day']
            wardrobeitem.value = form.cleaned_data['Value']
            wardrobeitem.color = form.cleaned_data['Color']
            wardrobeitem.gender = form.cleaned_data['Gender']
            wardrobeitem.size = form.cleaned_data['Size']
            wardrobeitem.start_year = form.cleaned_data['Start_Year']
            wardrobeitem.end_year = form.cleaned_data['End_Year']
            wardrobeitem.pattern = form.cleaned_data['Pattern']
            wardrobeitem.size_modifier = form.cleaned_data['Size_Modifier']
            wardrobeitem.save()
        return HttpResponseRedirect('/retail/rental.manageitems/')

    params['form'] = form
    params['wardrobeitem'] = wardrobeitem

    return templater.render_to_response(request, 'rental.editwardrobeitem.html', params)


class WardrobeEditForm(forms.Form):
    Name = forms.CharField(max_length=50, required=True, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Description = forms.CharField(max_length=200, required=False, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Category = forms.CharField(max_length=20, required=True, label='Category', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Rental_Price = forms.CharField(max_length=10, required=True, label='Rental Price', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Price_Per_Day = forms.CharField(max_length=10, required=True, label='Price Per Day', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Value = forms.CharField(max_length=10, required=True, label='Value', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Gender = forms.CharField(max_length=1, required=True, label='Gender', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Color = forms.CharField(max_length=10, required=True, label='Color', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Size = forms.CharField(max_length=10, required=True, label='Size', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Size_Modifier = forms.CharField(max_length=10, required=True, label='Size Modifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Pattern = forms.CharField(max_length=20, required=True, label='Pattern', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Start_Year = forms.DateField(required=True, label='Start Year', widget=forms.TextInput(attrs={'class': 'form-control'}))
    End_Year = forms.DateField(required=True, label='End Year', widget=forms.TextInput(attrs={'class': 'form-control'}))


@view_function
# @permission_required('admin.agent_rights', '/retail/login')
def create(request):

    wardrobe = request.urlparams[0]
    category = hmod.Category.objects.get(id=1)

    if wardrobe == 'wardrobe':
        wardrobeitem = hmod.WardrobeItem()
        wardrobeitem.name = ''
        wardrobeitem.description = ''
        wardrobeitem.category = category
        wardrobeitem.rental_price = 0.00
        wardrobeitem.price_per_day = 0.00
        wardrobeitem.value = 0.00
        wardrobeitem.color = ''
        wardrobeitem.gender = ''
        wardrobeitem.size = ''
        wardrobeitem.save()

        return HttpResponseRedirect('/retail/rental.editwardrobeitem/{}/'.format(wardrobeitem.id))

    if wardrobe == 'normal':
        rentableitem = hmod.RentableItem()
        rentableitem.name = ''
        rentableitem.description = ''
        rentableitem.category = category
        rentableitem.rental_price = 0.00
        rentableitem.price_per_day = 0.00
        rentableitem.value = 0.00
        rentableitem.save()

        return HttpResponseRedirect('/retail/rental.edit/{}/'.format(rentableitem.id))


@view_function
# @permission_required('admin.agent_rights', '/retail/login')
def delete(request):

    try:
        rentableitem = hmod.RentableItem.objects.get(id=request.urlparams[0])
        rentableitem.delete()
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/retail/rental.manageitems/')



    return HttpResponseRedirect('/retail/rental.manageitems/')


@view_function
# @permission_required('admin.agent_rights', '/retail/login')
def deletewardrobeitem(request):

    try:
        wardrobeitem = hmod.WardrobeItem.objects.get(id=request.urlparams[0])
        wardrobeitem.delete()
    except hmod.WardrobeItem.DoesNotExist:
        return HttpResponseRedirect('/retail/rental.manageitems/')

    return HttpResponseRedirect('/retail/rental.manageitems/')


@view_function
# @permission_required('admin.agent_rights' , '/homepage/login')
def manageitems(request):
    params = {}

    rentableitems = hmod.RentableItem.objects.all().order_by('name')
    wardrobeitems = hmod.WardrobeItem.objects.all().order_by('name')

    params['rentableitems'] = rentableitems
    params['wardrobeitems'] = wardrobeitems

    return templater.render_to_response(request, 'rental.manageitems.html', params)