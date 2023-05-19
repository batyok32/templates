from django.contrib.auth.models import Permission

from .filters import UserFilter
from .serializers import (
    PermissionSerializer,
    UserChangeSerializer,
    UserCreateeSerializer,
    UserListSerializer,
)
from rest_framework import generics
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny


class MyOffsetPagination(LimitOffsetPagination):
    """
    Custom Pagination Class
    """

    default_limit = 20
    max_limit = 1000


class PermissionsListView(generics.ListCreateAPIView):
    """
    List Permissions
    """

    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


class UserListCreateView(generics.ListCreateAPIView):
    """
    List And Create User
    """

    serializer_class = UserListSerializer
    queryset = User.objects.all()
    filter_backends = [SearchFilter, filters.DjangoFilterBackend]
    filterset_class = UserFilter
    search_fields = ["$username", "$id"]
    pagination_class = MyOffsetPagination
    # permission_classes = [AllowAny]

    def get_create_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = UserCreateeSerializer
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creating company usign username, password
        Creating company profile usign request.data and CompanyCreateSerializer
        """
        print("Creating user", request.data)
        serializer = self.get_create_serializer(data=request.data)
        print("SERIALIZER", serializer)
        if serializer.is_valid():
            try:
                print("Trying create user for user")
                username = request.data["username"]
                password = request.data["password"]
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("Created user")

                permissions = request.data["user_permissions"]
                print("ADDING PERMISSION")
                for perm in permissions:
                    val = perm["value"]
                    user.user_permissions.add(Permission.objects.get(id=val))
                print("ADDED PERMISSION")

            except:
                # print("Company already exists")
                return Response(
                    "User already exists", status=status.HTTP_400_BAD_REQUEST
                )
        else:
            print("Not correct profile form", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response("OK", status=status.HTTP_201_CREATED, headers=headers)


class UsersDestroyView(APIView):
    def post(self, request, *args, **kwargs):
        print("IN DELETE")
        users = request.data["users"]
        if users:
            for user in users:
                instance = User.objects.get(id=user)
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserChangeSerializer

    def get_update_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = UserChangeSerializer
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        # print("GOT OBJECT", instance)

        serializer = self.get_update_serializer(
            instance, data=request.data, partial=partial
        )
        # print("SERIALIZER", serializer)
        serializer.is_valid(raise_exception=True)
        # print("YEah it is valid")
        self.perform_update(serializer)

        permissions = request.data["user_permissions"]
        if permissions:
            print("ADDING PERMISSION")
            instance.user_permissions.clear()
            for perm in permissions:
                val = perm["value"]
                instance.user_permissions.add(Permission.objects.get(id=val))
            print("ADDED PERMISSION")

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
