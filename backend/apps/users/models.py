from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    display_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15, verbose_name='phone', blank=True)
    avatar = models.ImageField(upload_to="profile_images", default='profile_images/default.png', verbose_name='avatar')
    country = models.CharField(max_length=20, blank=True, default='', verbose_name='country')
    city = models.CharField(max_length=20, blank=True, default='', verbose_name='city')
