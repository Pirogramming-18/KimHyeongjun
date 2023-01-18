from django.shortcuts import render, redirect
from server.apps.posts.models import Post, DevTool
from django.http.request import HttpRequest

def ideas_list(request:HttpRequest, *args, **kwargs):
    posts = Post.objects.all()
    # text = request.GET.get("text")
    # if text:
    #     ideas = ideas.filter(content__contains=text)
    text = request.GET.get("text")
    if text:
        ideas = ideas.filter(content__contains=text)
    context = {
        "posts" : posts,
    }
    return render(request, "posts/ideas_list.html", context=context)

def devtool_list(request:HttpRequest, *args, **kwargs):
    devtools = DevTool.objects.all()
    text = request.GET.get("text")
    if text:
        devtools = devtools.filter(content__contains=text)
    context = {
        "devtools" : devtools,
    }
    return render(request, "posts/devtool_list.html", context=context)

def ideas_retrieve(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    # devtool = idea.devtool
    # all_idea = devtool.idea_devtool.all()
    devtool = post.devtool
    # all_post = user.post_set.all()
    all_post = devtool.post_devtool.all()

    devtool_name = post.devtool.name
    context = {
        "post" : post,
        "devtool_name" : devtool_name,
        "all_post" : all_post,
    }
    return render(request, "posts/ideas_retrieve.html", context=context)

def devtool_retrieve(request:HttpRequest, pk, *args, **kwargs):
    devtool = DevTool.objects.get(id=pk)
    # devtool = idea.devtool
    # all_idea = devtool.idea_devtool.all()
    context = {
        "devtool" : devtool,
    }
    return render(request, "posts/devtool_retrieve.html", context=context)

def ideas_create(request:HttpRequest, *args, **kwargs):
    devtools = DevTool.objects.all()
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            interest=request.POST["interest"],
            devtool=request.POST["devtool"],
            image=request.FILES['image'],
        )
        return redirect("/")
    context = {
        "devtools" : devtools
    }
    return render(request, "posts/ideas_create.html", context=context)

def devtool_create(request:HttpRequest, *args, **kwargs):
    if request.method == "POST":
        DevTool.objects.create(
            name=request.POST["name"],
            content=request.POST["content"],
            kind=request.POST["kind"],
        )
        return redirect("/")
    return render(request, "posts/devtool_create.html")

def ideas_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def devtool_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        devtool = DevTool.objects.get(id=pk)
        devtool.delete()
    return redirect("/")

def ideas_update(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title=request.POST["title"]
        post.content=request.POST["content"]
        post.interest=request.POST["interest"]
        post.devtool=request.POST["devtool"]
        post.image=request.FILES["image"]
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/posts_update.html", {"post":post})

def devtool_update(request:HttpRequest, pk, *args, **kwargs):
    devtool = DevTool.objects.get(id=pk)
    if request.method == "POST":
        devtool.name=request.POST["name"]
        devtool.content=request.POST["content"]
        devtool.kind=request.POST["kind"]
        devtool.save()
        return redirect(f"/posts/devtool/{devtool.id}")
    return render(request, "posts/devtool_update.html", {"devtool":devtool})



