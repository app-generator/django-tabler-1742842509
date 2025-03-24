# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    id = models.TextField(max_length=255, null=True, blank=True)
    first_name = models.TextField(max_length=255, null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)
    mid_name = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modificated = models.DateTimeField(blank=True, null=True, default=timezone.now)
    password = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Document(models.Model):

    #__Document_FIELDS__
    id = models.TextField(max_length=255, null=True, blank=True)
    parent_id = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data = models.TextField(max_length=255, null=True, blank=True)

    #__Document_FIELDS__END

    class Meta:
        verbose_name        = _("Document")
        verbose_name_plural = _("Document")



#__MODELS__END
