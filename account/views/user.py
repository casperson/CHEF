__author__ = 'Sterling'
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required
from .. import dmp_render_to_response, dmp_render
import datetime

templater = get_renderer('account')


@view_function
# @permission_required('admin.admin_rights' , '/homepage/login')
def process_request(request):
    params = {}

    users = hmod.User.objects.all().order_by('last_name')
    params['users'] = users

    return templater.render_to_response(request, 'user.html', params)

@view_function
# @permission_required('admin.manager_rights', '/homepage/login')
def edit(request):
    params ={}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
        address = hmod.Address.objects.get(user=user.id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/account/user/')

    form = UserEditForm(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'password': user.password,
        'address': address.address,
        'city': address.city,
        'state': address.state,
        'zip': address.zip,
        'phone': user.phone,
        'security_question': user.security_question,
        'security_answer': user.security_answer,

    })

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id

        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            address.address = form.cleaned_data['address']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.zip = form.cleaned_data['zip']
            user.phone = form.cleaned_data['phone']
            user.security_question = form.cleaned_data['security_question']
            user.security_answer = form.cleaned_data['security_answer']
            user.save()
            address.save()

            return HttpResponse('''
            <script>
                window.location.href = '/account/user/';
            </script>
            ''')

    params['form'] = form
    params['user'] = user
    params['address'] = address

    return dmp_render_to_response(request, 'user.edit.html', params)


class UserEditForm(forms.Form):
    username = forms.CharField(max_length=25, required=True, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label='Password')
    first_name = forms.CharField(max_length=20, required=True, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, required=True, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=50, required=True, label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=20, required=True, label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=2, required=True, label='State', widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip = forms.CharField(max_length=9, required=True, label='Zip Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=40, required=True, label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, required=True, label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    security_question = forms.CharField(max_length=100, required=True, label='Security Question', widget=forms.TextInput(attrs={'class': 'form-control'}))
    security_answer = forms.CharField(max_length=50, required=True, label='Security Answer', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("This username is already taken.")

        return self.cleaned_data['username']

        # if len(self.cleaned_data['username'])<5:
        #     raise forms.ValidationError("Please enter a username greater than 5 characters")
        # try:
        #     user = hmod.User.objects.get(username=self.cleaned_data['username'])
        #     raise forms.ValidationError("This Username is Already Taken. Please Enter a Different One")
        # except hmod.User.DoesNotExist:
        #     pass # we want this - this means it is free


@view_function
# @permission_required('admin.manager_rights', '/homepage/login')
def create(request):
    '''Create a new user'''
    user = hmod.User()
    user.username = ''
    user.password = ''
    user.first_name = ''
    user.last_name = ''
    user.phone = ''
    user.email = ''
    user.date_joined = datetime.datetime.now().date()
    user.security_question = ''
    user.security_answer = ''
    user.save()

    address = hmod.Address()
    address.address = ''
    address.city = ''
    address.state = ''
    address.zip = ''
    address.user = hmod.User.objects.get(id=user.id)
    address.save()

    return HttpResponseRedirect('/account/user.edit/{}/'.format(user.id))


@view_function
# @permission_required('admin.manager_rights', '/homepage/login')
def delete(request):

    print(request.urlparams[0])
    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
        user.delete()
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/account/user/')

    return HttpResponseRedirect('/account/user/')


