from django.http import HttpResponse
from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post


def text_response(request):
    return HttpResponse("Текстовое сообщение от приложения.")


def html_response(request):
    if request.method == 'GET':
        return render(request, 'template.html')

def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'GET':
        form = PostForm
        return render(request, 'post_create.html', context={'form': form})
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        rate = request.POST.get('rate')
        Post.objects.create(
            image=image,
            title=title,
            content=content,
            rate=rate
        )
        return redirect("/posts/")

