#coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

class Myuser(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined
    img = models.CharField(max_length='200', blank=False, null=False)
