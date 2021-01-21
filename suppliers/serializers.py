from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Supplier, Product
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class RegisterSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ("business_name", "address", "primary_full_name", "primary_email")
        write_only = ("auth_user",)

    def create(self, validated_data):
        username = validated_data["primary_email"]
        password = self.context["request"].data["password"]
        try:
            validators.validate_password(password=password, user=User)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(e)
        user = User.objects.create_user(username=username, password=password)
        validated_data["auth_user"] = user
        print(validated_data)
        return Supplier.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SupplierRetreiveSerializer(serializers.ModelSerializer):
    product_supplier = ProductSerializer(many=True)

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ("id", "auth_user", "primary_email", "created_at")


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250, required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "password")
