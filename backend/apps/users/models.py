import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename_new = "%s.%s" % (uuid.uuid4(), ext)
    return 'images/users/{filename_new}'.format(filename_new=filename_new)


class User(AbstractUser):
    display_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15, verbose_name='phone', blank=True)
    avatar = models.ImageField(upload_to=upload_to, blank=True,
                               null=True, max_length=500)
    country = models.CharField(max_length=20, blank=True, default='', verbose_name='country')
    city = models.CharField(max_length=20, blank=True, default='', verbose_name='city')
    email = models.EmailField(max_length=254, editable=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
