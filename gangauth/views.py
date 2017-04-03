import logging
import uuid

from django.views.generic import FormView, CreateView, TemplateView, UpdateView
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import resolve_url
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from gangauth.forms import UserLoginForm, UserSubscribeForm, UserGenerateLinkForm, UserUpdateForm
from gangdev.settings import base as settings
from gangdev.utils import User
from gangauth.utils import send_new_password


LOG = logging.getLogger("LOG")


class UserLoginView(FormView):
    """ Describe the User Login View """
    redirect_field_name = 'next'
    form_class = UserLoginForm
    template_name = "login.html"

    def get_success_url(self):
        """ Return the form's url """
        redirect_to = self.request.POST.get(self.redirect_field_name,
                                            self.request.GET.get(self.redirect_field_name, ''))

        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.request.META['HTTP_REFERER']
            if reverse('login') in redirect_to:
                return settings.LOGIN_REDIRECT_URL

        return redirect_to

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _(u'Login failed, username or password incorrect'), extra_tags="login")
        return super(UserLoginView, self).form_valid(form)

    def form_valid(self, form):
        """ Valid the form. """
        ret = super(UserLoginView, self).form_valid(form)
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        login(self.request, user)

        return ret


class UserCreateView(CreateView):
    """ Describe the User Creation View """
    redirect_field_name = 'next'
    form_class = UserSubscribeForm
    model = User
    template_name = 'user_subscribe.html'

    def get_success_url(self):
        """ Return the form's url """
        redirect_to = self.request.POST.get(self.redirect_field_name,
                                            self.request.GET.get(self.redirect_field_name, ''))

        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

        return redirect_to

    def get_form(self, form_class=None):
        """ Return the form object """
        form = super(UserCreateView, self).get_form()
        return form

    def form_valid(self, form):
        """ Valid the form. """
        form.instance.active = False
        ret = super(UserCreateView, self).form_valid(form)
        messages.success(self.request, "You are now registred")
        return ret


class UserUpdateView(UpdateView):  # pylint: disable=too-many-ancestors
    ''' Describe the User Update View '''
    form_class = UserUpdateForm
    template_name = 'user_edit.html'

    def get_object(self, queryset=None):
        ''' Return the request's user '''
        return self.request.user

    def get_success_url(self):
        ''' Return the success url '''
        return reverse('user_edit')


class UserForgotPasswordView(FormView):
    """
    Describe the forgot password view
    """
    form_class = UserGenerateLinkForm

    template_name = 'user_password_forgot.html'
    success_url = reverse_lazy("password_forgot")

    def form_valid(self, form):
        user = User.objects.filter(username=form.cleaned_data['username'])
        context = self.get_context_data(form=form)
        if len(user) == 1:
            send_new_password(user.first())
            context['mail_send'] = True
        else:
            context['mail_send'] = False

        return self.render_to_response(context)
