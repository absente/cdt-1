from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRel
from django.contrib.contenttypes.models import ContentType


@python_2_unicode_compatible
class Account(models.Model):
    username = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=64, null=True, unique=True)
    password = models.CharField(max_length=128, null=True)
    user_type = models.CharField(max_length=32)
    is_active = models.BooleanField()
    last_login = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_account(cls, username, password, user_type, email):

        account = cls.objects.create(
            username=username,
            password=password,
            email=email,
            is_active=True,
            user_type=user_type,
        )
        account.save()

    def __str__(self):
        return self.email
