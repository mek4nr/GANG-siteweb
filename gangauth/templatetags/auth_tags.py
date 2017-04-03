from django import template
register = template.Library()


@register.filter
def has_login_message(messages):
    for message in messages:
        if message.extra_tags == "login":
            return True
    return False
