from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')


@view_function
# @permission_required('admin.manager_rights', '/homepage/login/')
def process_request(request):
    params = {}

    params['events'] = hmod.Event.objects.all().order_by('start_date')

    return templater.render_to_response(request, 'events.view.html', params)


@view_function
# @permission_required('admin.admin_rights', '/homepage')
def edit(request):
    params = {}

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events.manage')

    form = EventEditForm(initial={

        'name': event.name,
        'description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date,
    })

    if request.method == 'POST':
        print(request.method)
        form = EventEditForm(request.POST)
        if form.is_valid():

            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.save()

            return HttpResponseRedirect('/homepage/events.manage')


    params['form'] = form
    params['event'] = event
    return templater.render_to_response(request, 'events.edit.html', params)


class EventEditForm(forms.Form):
    name = forms.CharField(required=True, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(required=True, label='Start Date', widget=forms.DateInput(attrs={'class': 'form-control'}))
    end_date = forms.DateField(required=True, label='End Date', widget=forms.DateInput(attrs={'class': 'form-control'}))

    # def clean_username(self):
    #   if len(self.cleaned_data['username']) < 5
    #       raise forms.ValidationError("Please enter a username greater than 5 characters")
    #   try:
    #       event = hmod.Event.objects.get(event=self.cleaned_data['username'])
    #       raise forms.ValidationError("This username is already taken")
    #   except hmod.Event.DoesNotExist:
    #       pass #we want this because it meas that the username is free


@view_function
# @permission_required('admin.admin_rights', '/homepage')
def create(request):
    event = hmod.Event()
    event.name = ''
    event.description = ''
    event.start_date = '1901-1-1'
    event.end_date = '1901-1-1'
    event.address = hmod.Address.objects.get(id=2)
    event.save()

    return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event.id))


@view_function
# @permission_required('admin.admin_rights', '/homepage')
def delete(request):

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
        event.delete()
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events.manage/')

    return HttpResponseRedirect('/homepage/events.manage/')


@view_function
# @permission_required('admin.manager_rights', '/homepage/login/')
def details(request):
    params = {}

    try:
        areas = hmod.Area.objects.all().filter(event=request.urlparams[0])
        event = hmod.Event.objects.get(id=request.urlparams[0])
        products = hmod.Product.objects.all()
      #  supername = hmod.Area.supername(request.urlparams[0])

    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/events')

    params['areas'] = areas
    params['event'] = event
    params['products'] = products

    # params['supername'] = supername

    return templater.render_to_response(request, 'events.detail.html', params)

@view_function
# @permission_required('admin.admin_rights', '/homepage')
def manage(request):
    params = {}

    params['events'] = hmod.Event.objects.all().order_by('start_date')

    return templater.render_to_response(request, 'events.html', params)