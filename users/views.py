from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework.views import APIView


from .serializers import (
    UserSerializer,
    CreateUserSerializer,
    LoginSerializer,
    MyTokenObtainPairSerializer,
)

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken, AuthenticationFailed
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer
    http_method_names = ['post']

    @swagger_auto_schema(request_body=CreateUserSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'message': 'User created successfully', 'token': token}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    http_method_names = ['post']

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = User.objects.get(username=username)
        if user.check_password(password):
            token = get_tokens_for_user(user)
            return Response({'message': 'User logged in successfully', 'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer