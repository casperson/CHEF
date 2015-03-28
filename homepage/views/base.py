from django.conf import settings
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from homepage import dmp_render, dmp_render_to_response
from django import forms
from django.contrib.auth import authenticate, login, logout


@view_function
def process_request(request):
    template_vars = {}

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # authenticate and login
            pass

    template_vars['form'] = form
    return dmp_render_to_response(request, 'base.html', template_vars)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is None:
            raise forms.ValidationError('Invalid username or password.')
        return self.cleaned_data


@view_function
def loginform(request):
    template_vars = {}

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # authenticate and login
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('''
            <script>
                window.location.href = window.location.href;
            </script>
            ''')

    template_vars['form'] = form
    return dmp_render_to_response(request, 'base.loginform.html', template_vars)