from django.conf import settings
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from homepage import dmp_render, dmp_render_to_response
from django import forms
import homepage.models as hmod
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE, GET_ALL_INFO
import json

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
    username = forms.CharField(max_length=25, required=True, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label='Password')

    def clean(self):
        # s = Server('ldap.forumsys.com', port = 389, get_info = GET_ALL_INFO)
        # c = Connection(cn='read-only-admin',uid=gauss,password=password)
        uName = self.cleaned_data['username']
        pWord = self.cleaned_data['password']
        fullName = uName+'@thecolonialheritage.local'
        try:
            s = Server('128.187.61.50', port=9000, get_info=GET_ALL_INFO)
            c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user=fullName, password=pWord, authentication=AUTH_SIMPLE, raise_exceptions=False)
            search_results = c.search(
            search_base='CN=Users,DC=thecolonialheritage,DC=local',
            search_filter='(samAccountName=uName)',
            attributes=[
                'givenName',
                'sn',
            ])
            # user_info = c.response[0]['attributes']
            # print(search_results)
            # print("user info is next!")
            # print(user_info)
            # print(json.loads(c.response_to_json(search_results)))['entries'][0]['attributes']
            user, created = hmod.User.objects.get_or_create(username=uName)
            # user.first_name = search_results.givenName
            # user.last_name = search_results.sn
            #  u.email = c.email
            user.set_password(pWord)
            user.save()
        except :
            pass
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
            uName = form.cleaned_data['username']
            pWord = form.cleaned_data['password']
            fullName = uName+'@thecolonialheritage.local'
            print(fullName)
            print(pWord)
            # s = Server('128.187.61.50', port=9000, get_info=GET_ALL_INFO)
            # c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user=fullName, password='IhaveANenglishdegr33', authentication=AUTH_SIMPLE, raise_exceptions=False)
            # print(s.info) # display info from the DSE. OID are decoded when recognized by the library
            # print(">>>>> print connection results")
            # print(c.result)
            # print(c.response) #it's okay if this is None
            # s = Server('128.187.61.50', port=9000, get_info=GET_ALL_INFO)
            # c = Connection(s, auto_bind=False, client_strategy=STRATEGY_SYNC, user=fullName, password=pWord, authentication=AUTH_SIMPLE)
            # # if c:
            #     # pass
            #
            #     newUser = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            #     login(request, newUser)
            # else:
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('''
            <script>
                window.location.href = window.location.href;
            </script>
            ''')

    template_vars['form'] = form
    return dmp_render_to_response(request, 'base.loginform.html', template_vars)