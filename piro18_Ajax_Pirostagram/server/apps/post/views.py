from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    ctx = {
        'posts' : posts,
        'comments' : comments,
    }
    return render(request, 'post_list.html', ctx)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
        else:
            ctx = {
                'form': form
            }
            return render(request, 'post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        context = {
            'form' : form,
        }
        return render(request, 'post_new.html', ctx)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    post = Post.objects.get(id = post_id)

    if post.like == True:
        post.like = False
    else:
        post.like = True
    post.save()
    type = post.like
    return JsonResponse({'id': post_id, 'type': type})
