from rest_framework import serializers
from cdtAction.models import Account


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        models = Account
        depth = 0
