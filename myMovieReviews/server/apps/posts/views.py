from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from server.apps.posts.models import Post

def movie_list(request: HttpRequest, *args, **kwards):
    movies = Post.objects.all()
    return render(request, "posts/movie_list.html", {"movies": movies})

def movie_retrieve(request: HttpRequest, pk, *args, **kwargs):
    movie = Post.objects.all().get(id=pk)
    return render(request, "posts/movie_retrieve.html", {"movie": movie})

def movie_create(request: HttpRequest, *args, **kwargs):
    print(request.method)
    if request.method == "POST":
        Post.objects.create(
            movie_title=request.POST["movie_title"],
            movie_genre=request.POST["movie_genre"],
            running_time=request.POST["running_time"],
            review_content=request.POST["review_content"],
            director=request.POST["director"],
            actor=request.POST["actor"],
            rating=request.POST["rating"],
            movie_created_at=request.POST["movie_created_at"],
        )
        return redirect("/")
    return render(request, "posts/movie_create.html")

def movie_update(request: HttpRequest, pk, *args, **kwargs):
    movie = Post.objects.get(id=pk)
    if request.method == "POST":
        movie.movie_title=request.POST["movie_title"]
        movie.movie_genre=request.POST["movie_genre"]
        movie.running_time=request.POST["running_time"]
        movie.review_content=request.POST["review_content"]
        movie.director=request.POST["director"]
        movie.actor=request.POST["actor"]
        movie.rating=request.POST["rating"]
        movie.movie_created_at=request.POST["movie_created_at"]
        movie.save()
        return redirect(f"/posts/{movie.id}")
    return render(request, "posts/movie_update.html", {"movie": movie})

def movie_delete(request: HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        movie = Post.objects.get(id=pk)
        movie.delete()
    return redirect("/")