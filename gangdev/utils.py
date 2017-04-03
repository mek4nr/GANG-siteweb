from django.conf import settings
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage, get_connection

user_app_name, user_model_name = settings.AUTH_USER_MODEL.rsplit('.', 1)
User = None
try:
    User = apps.get_registered_model(user_app_name, user_model_name)
except KeyError:
    pass
if User is None:
    raise ImproperlyConfigured(
        "You have defined a custom user model %s, but the app %s is not "
        "in settings.INSTALLED_APPS" % (settings.AUTH_USER_MODEL, user_app_name)
    )


def send_mail(subject, body, to):

    # Setup the smtp connection with conf file
    smtp_data = {
        "host": settings.EMAIL_HOST,
        "port": settings.EMAIL_POST,
        "username": settings.EMAIL_HOST_USER,
        "password": settings.EMAIL_HOST_PASSWORD,
        "use_tls": settings.EMAIL_USE_TLS,
    }

    # Setup mail with all data need it
    mail = {
        "subject": subject,
        "body": body,
        "from_email": settings.EMAIL_FROM,
        "to": to,
        "connection": get_connection(**smtp_data)
    }

    msg = EmailMessage(**mail)
    msg.content_subtype = "html"
    msg.send()
