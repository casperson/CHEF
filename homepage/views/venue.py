__author__ = 'Sterling'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')


@view_function
@permission_required('admin.manager_rights' , '/homepage/login')
def process_request(request):
    params = {}

    venues = hmod.Venue.objects.all().order_by('name')
    params['venues'] = venues

    return templater.render_to_response(request, 'venue.html', params)

@view_function
@permission_required('admin.manager_rights', '/homepage/login')
def edit(request):
    params ={}

    try:
        venue = hmod.Venue.objects.get(id=request.urlparams[0])
    except hmod.Venue.DoesNotExist:
        return HttpResponseRedirect('/homepage/venue/')

    form = VenueEditForm(initial={
        'name': venue.name,
        'address':venue.address,
        'city': venue.city,
        'state': venue.state,
        'zip': venue.zip,
    })

    if request.method == 'POST':
        form = VenueEditForm(request.POST)
        if form.is_valid():
            venue.name = form.cleaned_data['name']
            venue.address = form.cleaned_data['address']
            venue.city = form.cleaned_data['city']
            venue.state = form.cleaned_data['state']
            venue.zip = form.cleaned_data['zip']
            venue.save()
            return HttpResponseRedirect('/homepage/venue/')

    params['form'] = form
    params['venue'] = venue
    return templater.render_to_response(request, 'venue.edit.html', params)


class VenueEditForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    address = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=20, required=True)
    state = forms.CharField(max_length=10, required=True)
    zip = forms.CharField(max_length=10, required=True)


@view_function
@permission_required('admin.manager_rights', '/homepage/login')
def create(request):
    '''Create a new venue'''
    venue = hmod.Venue()
    venue.name = ''
    venue.address = ''
    venue.city = ''
    venue.state = ''
    venue.zip = ''
    venue.save()

    return HttpResponseRedirect('/homepage/venue.edit/{}/'.format(venue.id))


@view_function
@permission_required('admin.manager_rights', '/homepage/login')
def delete(request):

    try:
        venue = hmod.Venue.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/venue/')

    venue.delete()

    return HttpResponseRedirect('/homepage/venue/')

