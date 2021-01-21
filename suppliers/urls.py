from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("register/", RegisterSupplierAPI.as_view()),
    path("", SupplierListAPI.as_view()),
    path("<int:pk>/", ProfileView.as_view()),
    path("update/<int:pk>/", SuppplierUpdateAPI.as_view()),
    path("login/", Login.as_view()),
    path("logout/", Logout.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
