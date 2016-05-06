from rest_framework import viewsets
from cdtAction.models import Account
from cdtAction.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    user = Account.objects.all()
    print(user)
    serializer_class = UserSerializer
