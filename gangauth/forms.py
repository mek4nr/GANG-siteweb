from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext as _
from gangdev.utils import User
from simplemathcaptcha.fields import MathCaptchaField


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserSubscribeForm(UserCreationForm):
    captcha = MathCaptchaField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserGenerateLinkForm(forms.Form):
    username = forms.CharField(max_length=254)


class UserUpdateForm(forms.ModelForm):

    class Meta:  # pylint: disable=too-few-public-methods
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
