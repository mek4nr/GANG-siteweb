from django.conf.urls import url
from django.contrib.auth.views import password_change, password_change_done
from gangauth.views import UserLoginView, UserCreateView, UserUpdateView, UserForgotPasswordView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^in/?$', UserLoginView.as_view(), {'redirect_field_name': 'next'}, name="login"),
    url(r'^edit/?$', login_required(UserUpdateView.as_view()), name='user_edit'),
    url(r'^password/reset/?$', login_required(password_change), {'template_name': 'user_password_reset.html'}, name='user_password'),
    url(r'^password/done/?$', login_required(password_change_done), {'template_name': 'user_password_done.html'}, name="password_change_done"),
    url(r'^password/forgot/?$', UserForgotPasswordView.as_view(), name="password_forgot"),
    url(r'^out/?$', logout, {'next_page': '/'}, name="logout"),
    url(r'^up/?$', UserCreateView.as_view(), name="subscribe"),
]
