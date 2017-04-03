import uuid
from django.db import models
from django.core.urlresolvers import reverse
from gangdev.settings.base import DOMAIN_NAME


class EmailCheck(models.Model):
    user = models.ForeignKey("auth.User")
    token = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}" . format(self.user)

    def __unicode__(self):
        return self.__str__()

    def is_alive(self):
        return True

    def active_link(self):
        return "{}{}" .format(DOMAIN_NAME, reverse("active", kwargs={
                                'token': str(self.token),
                                'username': self.user.username,
                                }))

    def check_token(self):
        if self.is_alive():
            self.user.is_active = True
            self.user.save()
            return True
        else:
            return False