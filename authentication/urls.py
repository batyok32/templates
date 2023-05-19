from django.urls import path
from . import views

urlpatterns = [
    path("permissions/", views.PermissionsListView.as_view()),
    path("users/", views.UserListCreateView.as_view()),
    path("users/<int:pk>/", views.UserUpdateView.as_view()),
    path("users/delete/", views.UsersDestroyView.as_view()),
]
