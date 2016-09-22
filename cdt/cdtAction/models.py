from __future__ import unicode_literals
import random

from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import authenticate


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nikename = models.CharField(max_length=255, help_text='nike name')
    email = models.EmailField(max_length=255, help_text='email')
    mobile_no = models.CharField(max_length=255, help_text='mobile_no')

    def __str__(self):
        fileds = [self.user, self.email]

        return ' '.join([str(r) for r in fileds])

    def create_account(self):
        while True:
            dt = timezone.now()
            username = '{}{}'.format(int(dt.timestamp()), random.randint(0, 1000))
            check_sum = sum(int(r) for r in username) % 10
            if check_sum != 0:
                check_sum = 10 - check_sum
            user, is_user = User.objects.get_or_create(username='{}{}'.format(username, check_sum))
            if is_user:
                return user


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
