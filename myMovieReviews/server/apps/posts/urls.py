from django.urls import path

from server.apps.posts.views import movie_list, movie_retrieve, movie_create, movie_update, movie_delete

urlpatterns = [
    path("", movie_list),
    path("posts/create", movie_create),
    path("posts/<int:pk>", movie_retrieve),
    path("posts/<int:pk>/update", movie_update),
    path("posts/<int:pk>/delete", movie_delete),
]
