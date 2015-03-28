__author__ = 'Sterling'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django.contrib.auth import authenticate, login
from django_mako_plus.controller.router import get_renderer
from django import forms

templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, user)
                return HttpResponseRedirect('/homepage/account/')

    params['form'] = form
    return templater.render_to_response(request, 'login.html', params)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is None:
            raise forms.ValidationError('Invalid username or password.')
        return self.cleaned_data
