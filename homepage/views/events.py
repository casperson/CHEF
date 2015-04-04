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
##@permission_required('admin.manager_rights', '/homepage/login/')

def process_request(request):

    params = {}

    params['events'] = hmod.Event.objects.all().order_by('start_date')

    return templater.render_to_response(request, 'events.html', params)

########## Edit
@view_function
##@permission_required('admin.manager_rights', '/homepage/login/')

def edit(request):

    params = {}

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events')

    form = EventEditForm(initial={

        'name': event.name,
        'description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date,

    })
    if request.method == 'POST':
        form = EventEditForm(request.POST)
        if form.is_valid():
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.save()
            return HttpResponseRedirect('/homepage/events')


    params['form'] = form
    return templater.render_to_response(request, 'events.edit.html', params)


class EventEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    description = forms.CharField(required=True, max_length=300)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)

    # def clean_username(self):
    #   if len(self.cleaned_data['username']) < 5
    #       raise forms.ValidationError("Please enter a username greater than 5 characters")
    #   try:
    #       event = hmod.Event.objects.get(event=self.cleaned_data['username'])
    #       raise forms.ValidationError("This username is already taken")
    #   except hmod.Event.DoesNotExist:
    #       pass #we want this because it meas that the username is free


### create new
@view_function
##@permission_required('admin.manager_rights', '/homepage/login/')

def create(request):

    event = hmod.Event()
    event.name = ''
    event.description = ''
    event.start_date = '1901-1-1'
    event.end_date = '1901-1-1'
    event.save()

    return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event.id))

### delete
@view_function
##@permission_required('admin.manager_rights', '/homepage/login/')

def delete(request):

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect('/homepage/events')

    event.delete()

    return HttpResponseRedirect('/homepage/events/')


@view_function
##@permission_required('admin.manager_rights', '/homepage/login/')

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