__author__ = 'Sterling'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required, login_required

templater = get_renderer('homepage')


@view_function
@permission_required('admin.agent_rights' , 'base.loginform.html')
def process_request(request):
    params = {}

    items = hmod.Item.objects.all().order_by('name')
    params['items'] = items

    return templater.render_to_response(request, 'item.html', params)


@view_function
@permission_required('admin.agent_rights', 'base.loginform.htmln')
def edit(request):
    params ={}

    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/item/')

    form = ItemEditForm(initial={
        'name': item.name,
        'description':item.description,
        'value': item.value,
        'standard_rental_price': item.standard_rental_price
    })

    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.value = form.cleaned_data['value']
            item.standard_rental_price = form.cleaned_data['standard_rental_price']
            item.save()
            return HttpResponseRedirect('/homepage/item/')

    params['form'] = form
    params['item'] = item
    return templater.render_to_response(request, 'item.edit.html', params)


class ItemEditForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=200, required=False)
    value = forms.CharField(max_length=20, required=True)
    standard_rental_price = forms.CharField(max_length=10, required=False)


@view_function
@permission_required('admin.agent_rights', 'base.loginform.html')
def create(request):
    '''Create a new item'''
    item = hmod.Item()
    item.name = ''
    item.description = ''
    item.value = 0.00
    item.standard_rental_price = 0.00
    item.save()

    return HttpResponseRedirect('/homepage/item.edit/{}/'.format(item.id))


@view_function
@permission_required('admin.agent_rights', 'base.loginform.html')
def delete(request):

    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/item/')

    item.delete()

    return HttpResponseRedirect('/homepage/item/')

