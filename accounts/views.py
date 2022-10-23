# Django packages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# DRF packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Local apps
from .serializers import UserRegisterSerializer, UserLoginSerializer


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            ser_validate_data = ser_data.validated_data
            User.objects.create_user(
                username=ser_validate_data['username'],
                password=ser_validate_data['password']
            )
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            ser_validate_data = ser_data.validated_data
            user = authenticate(
                request, username=ser_validate_data['username'], password=ser_validate_data['password']
            )
            if user is not None:
                login(request, user)
                return Response(ser_data.data, status=status.HTTP_200_OK)
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
