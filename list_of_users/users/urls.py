from django.urls import path

from users.views import *

urlpatterns = [
    path("", ListUsers.as_view(), name="list_of_users"),
    path("users/<int:pk>/", ViewUser.as_view(), name="users"),
    path("users/add_user/", CreateUser.as_view(), name="add_user"),
    path("users/edit_user/<int:pk>/", UpdateUser.as_view(), name="edit_user"),
    path("users/delete_user/<int:pk>/", DeleteUser.as_view(), name="delete_user"),
]
