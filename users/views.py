from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.migrations.serializer import UserCreateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(username=serializer.validated_data['username'],
                                    password=serializer.validated_data['password']
                                    )
    return Response(data={'user.id': user.id}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def authorization_api_view(request):
    serailizer = UserLoginSerializer(data=request.data)
    serailizer.is_valid(raise_exception=True)
    user = authenticate(**serailizer.validated_data)
    if user:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,data={'error': 'User does not exist!'})