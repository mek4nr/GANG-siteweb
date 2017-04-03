#!/usr/bin/env python
from random import choice, shuffle
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation
)
from django.template.loader import get_template
from django.template import Context
from gangauth.models import EmailCheck
from gangdev.utils import send_mail
from gangdev.settings.base import DOMAIN_NAME


LENGTH = 10
MIN_LOWERCASE = 2
MIN_UPPERCASE = 2
MIN_DIGITS = 2
MIN_SPECIAL = 1


def send_new_password(user):
    password = mkpasswd()

    user.set_password(password)
    user.save()

    htmly = get_template("emails/forgot_password_email.html")
    context = {
        "password": password,
        "url": DOMAIN_NAME
    }
    html_content = htmly.render(Context(context))

    mail = {
        "subject": "Password forgot",
        "body": html_content,
        "to": [user.email],
    }
    send_mail(**mail)


def mkpasswd(length=LENGTH,
             min_lower=MIN_LOWERCASE,
             min_upper=MIN_UPPERCASE,
             min_digits=MIN_DIGITS,
             min_special=MIN_SPECIAL):
    """
    Generate password
    :param length: Size of password
    :param min_lower: Min char on lower case
    :param min_upper: Min char on lower case
    :param min_digits: Min digits
    :param min_special: Min special char
    :return: Password
    """
    lower = [choice(ascii_lowercase) for i in range(min_lower)]
    upper = [choice(ascii_uppercase) for i in range(min_upper)]
    nums = [choice(digits) for i in range(min_digits)]
    special = [choice(punctuation) for i in range(min_special)]

    minimum = min_lower + min_upper + min_digits + min_special
    remaining = (length - minimum) if length > minimum else 0
    rest = [choice(ascii_letters) for i in range(remaining)]

    result = upper + lower + nums + special + rest
    shuffle(result)

    return ''.join(result)


def email_for_active_count(user):
    """
    Send mail with active link
    """
    email_check = EmailCheck.objects.create(user=user)
    htmly = get_template("emails/active_email.html")

    context = {
        "email": user.email,
        "active_link": email_check.active_link()
    }
    html_content = htmly.render(Context(context))

    # Setup mail with all data need it
    mail = {
        "subject": "Welcome to IBISC Platform",
        "body": html_content,
        "to": [user.email],
    }

    send_mail(**mail)
