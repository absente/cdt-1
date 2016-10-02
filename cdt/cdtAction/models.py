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
    email = models.EmailField(max_length=255, help_text='email', db_index=True)
    mobile_no = models.CharField(max_length=255, help_text='mobile_no', db_index=True)

    def __str__(self):
        fileds = [self.user, self.email]

        return ' '.join([str(r) for r in fileds])

    @classmethod
    def create_account(cls, nikename='', email='', mobile_no=''):
        dt = timezone.now()
        username = '{}{}'.format(int(dt.timestamp()), random.randint(0, 1000))
        if not email and not mobile_no:
            return cls.objects.none()
        elif email and mobile_no:
            email = email
            mobile_no = mobile_no
        elif not email or not mobile_no:
            email = email if email else '{}@null_cdt.com'.format(username)
            mobile_no = mobile_no if mobile_no else username

        check_sum = sum(int(r) for r in username) % 10
        if check_sum != 0:
            check_sum = 10 - check_sum
        user, is_user = User.objects.get_or_create(username='{}{}'.format(username, check_sum))
        if is_user:
            cls(user=user, email=email, mobile_no=mobile_no)
            user.email = email
            return user

    @classmethod
    def login(cls, requests):
        user = requests.user
        if not user:
            return False

