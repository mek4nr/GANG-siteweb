from django.db import models
from django.contrib.auth.models import AbstractUser
from filer.fields.image import FilerImageField


class User(AbstractUser):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    sex = models.CharField(choices=SEX_CHOICES, max_length=1, null=True, blank=True)
    profil_picture = FilerImageField(null=True, blank=True)

    def get_profil_folder(self):
        """
        :return: The folder who image will be stored
        """
        return u"User/{}". \
            format(self.pk)

    def __unicode__(self):
        ''' Return the username '''
        return self.username

    def __str__(self):
        ''' Return the username '''
        return self.__unicode__()
