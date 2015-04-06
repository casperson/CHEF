from django.conf import settings
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from homepage import dmp_render, dmp_render_to_response
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO


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
        # s = Server('ldap.forumsys.com', port = 389, get_info = GET_ALL_INFO)
        # c = Connection(cn='read-only-admin',uid=gauss,password=password)
        uname=self.cleaned_data['username']
        pword=self.cleaned_data['password']
        s = Server('128.187.61.50', port = 9000, get_info = GET_ALL_INFO)
        c = Connection(s, auto_bind = False, client_strategy = STRATEGY_SYNC, user=uname, password=pword, authentication=AUTH_SIMPLE)
        if c is not None:
            pass
            # u = hmod.User.objects.get_or_create(username=uname)
            # u.first_name = c.first_name
            # u.last_name = c.last_name
            # u.email = c.email
            # u.set_password(pword)
            # u.save()

            # user = authenticate(uname, pword)
        else:    
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
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('''
            <script>
                window.location.href = window.location.href;
            </script>
            ''')

    template_vars['form'] = form
    return dmp_render_to_response(request, 'base.loginform.html', template_vars)