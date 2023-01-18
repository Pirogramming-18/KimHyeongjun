from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.ideas_list, name="list"),
    path("posts/devtool", views.devtool_list, name="dTList"),
    path("posts/create", views.ideas_create, name="create"),
    path("posts/devtool/create", views.devtool_create, name="dTCreate"),
    path("posts/<int:pk>", views.ideas_retrieve, name="retrieve"),
    path("posts/devtool/<int:pk>", views.devtool_retrieve, name="dTRetrieve"),
    path("posts/<int:pk>/update", views.ideas_update, name="update"),
    path("posts/devtool/<int:pk>/update", views.devtool_update, name="dTUpdate"),
    path("posts/<int:pk>/delete", views.ideas_delete, name="delete"),
    path("posts/devtool/<int:pk>/delete", views.devtool_delete, name="dTDelete"),
]