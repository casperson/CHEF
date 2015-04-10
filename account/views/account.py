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
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('account')


@view_function
# @permission_required('admin.admin_rights' , '/homepage/login')
def process_request(request):
    params = {}

    cart = hmod.ShoppingCart.objects.get(user_id=request.user.id)
    lineitems = hmod.LineItem.objects.all().filter(shopping_cart=cart, product=None, return_line_item=None)

    params['lineitems'] = lineitems

    return templater.render_to_response(request, 'account.html', params)


@view_function
# @permission_required('admin.manager_rights', '/homepage/login')
def changepassword(request):
    params = {}

    try:
        user = hmod.User.objects.get(id=request.user.id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/account/user/')

    form = ChangePasswordForm(initial={
        'password': user.password,
        'newpassword': request.POST.get('newpassword'),
        'checkpassword': request.POST.get('checkpassword')

    })

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        form.userid = user.id

        if form.is_valid():
            username = user.username
            newpassword = form.cleaned_data['newpassword']
            checkpassword = form.cleaned_data['checkpassword']
            if newpassword == checkpassword:
                user.set_password(form.cleaned_data['newpassword'])
                user.save()
                user = authenticate(username=username, password=form.cleaned_data['newpassword'])
                login(request, user)
            else:
                raise forms.ValidationError("The new password does not match.")

        return HttpResponse('''
            <script>
                window.location.href = window.location.href;
            </script>
            ''')

    params['form'] = form
    params['user'] = user

    return templater.render_to_response(request, 'account.changepassword.html', params)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label='Current Password')
    newpassword = forms.CharField(max_length=25, required=True, label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    checkpassword = forms.CharField(max_length=25, required=True, label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def clean_password(self):
    #     if 'newpassword' in self.cleaned_data and 'checkpassword' in self.cleaned_data:
    #         if self.cleaned_data['newpassword'] != self.cleaned_data['checkpassword']:
    #             raise forms.ValidationError('The entered passwords do not match.')
    #     return self.cleaned_data['newpassword']

    # def clean_password(self):
    #     cleaned_data = authenticate(ChangePasswordForm, self).clean()
    #     if cleaned_data['newpassword'] != cleaned_data['checkpassword']:
    #         raise forms.ValidationError('The entered passwords do not match.')
    #     return cleaned_data['newpassword']


@view_function
def logout_user(request):

    logout(request)

    return HttpResponseRedirect('/homepage/')