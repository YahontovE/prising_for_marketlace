from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import IsSuperuser
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания(регистрация) юзера"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех юзеров"""
    serializer_class = UserSerializer
    permission_classes =[IsSuperuser]
    queryset = User.objects.all()