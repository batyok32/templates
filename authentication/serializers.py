# from django.db.models import fields
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Permission

User = get_user_model()


# For Sign up and list


class UserCreateeSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "username", "password")


class UserChangeSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "username", "password")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "date_joined",
        )


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            "id",
            "name",
            "codename",
        )


# Detail User
class UserDetailSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "last_login",
            "user_permissions",
        )
