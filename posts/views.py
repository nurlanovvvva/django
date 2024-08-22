from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def text_response(request):
    return HttpResponse("Текстовое сообщение от приложения.")


def html_response(request):
    return render(request, 'template.html')

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})
