from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from .serializers import UserLoginSerializer, RegisterSupplierSerializer, SupplierRetreiveSerializer, SupplierUpdateSerializer
from .models import Supplier

# Create your views here.

class RegisterSupplierAPI(CreateAPIView):
    """
    Register Supplier API

        Data : {
                    "primary_email":"sandeep6@gmail.com",
                    "business_name":"business_name",
                    "password":"Sand@123",
                    "address":"address",
                    "primary_full_name":"name"
                }
    """
    serializer_class = RegisterSupplierSerializer
    queryset = Supplier.objects.all()


class Login(TokenObtainPairView, APIView):
    """
    Login POST API

        Data : {
            "username" : username,
            "password" : password
        }

        Response : {
                        "account_id": account_id,
                        "refresh": Refresh Token,
                        "access": access_token,
                    }
    """

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = authenticate(
                    username=data["username"], password=data["password"]
                )
                if user:
                    supplier_id=user.id
                    print(user.supplier.all())
                    if user.supplier.all():
                        supplier_id = user.supplier.get().id
                    refresh = RefreshToken.for_user(user)
                    is_admin = user.is_superuser
                    return Response(
                        {
                            "account_id": supplier_id,
                            "is_admin":is_admin,
                            "refresh": str(refresh),
                            "access": str(refresh.access_token),
                        },
                        status=status.HTTP_200_OK,
                    )
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)


class Logout(APIView):
    """
    Logout DELETE API

        Data : {
            "refresh" : refresh_token
        }

        Response : {
                status = 204
        }
    """

    # permission_classes = (IsAuthenticated,)

    def delete(self, request):
        try:
            data = request.data
            token = RefreshToken(data["refresh"])
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

class ProfileView(RetrieveAPIView):
    """
    Retreive API view for Supplier Profile
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SupplierRetreiveSerializer
    queryset = Supplier.objects.all()

class SupplierListAPI(ListAPIView):
    """
    List APi for all suppliers
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SupplierRetreiveSerializer
    queryset = Supplier.objects.all()

class SuppplierUpdateAPI(UpdateAPIView):
    """
    Update API for Supplier
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SupplierUpdateSerializer
    queryset = Supplier.objects.all()