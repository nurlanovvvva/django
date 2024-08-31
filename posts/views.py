from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from posts.forms import PostForm, PostForm2, SearchForm
from posts.models import Post


def text_response(request):
    return HttpResponse("Текстовое сообщение от приложения.")


def html_response(request):
    if request.method == 'GET':
        return render(request, 'template.html')


@login_required(login_url='login')
def post_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search', None)
        tag = request.GET.getlist('tag', None)
        orderings = request.GET.get('orderings')
        search_form = SearchForm(request.GET)
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(tag__icontains=search))
        if tag:
            posts = posts.filter(tag__id__in=tag)
        if orderings:
            posts = posts.order_by(orderings)
            print(request.GET)
        limit = 5
        max_page = posts.count()/ limit
        if round(max_page)<max_page:
            max_page = round(max_page)+1
        else:
            max_page = round(max_page)
            start = (page-1)*limit
            end = (page)*limit
            posts = posts[start:end]

        context = {'posts': posts, 'search_form': search_form, 'max_page':range(1, max_page+1)}
        return render(request, 'post_list.html', context=context)


@login_required(login_url='login')
def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'post_detail.html', {'post': post})


@login_required(login_url='login')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'post_create.html', {'form': form})
        image = form.cleaned_data.get('image')
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        rate = form.cleaned_data.get('rate')
        Post.objects.create(
            image=image,
            title=title,
            content=content,
            rate=rate
        )
        return redirect("/posts/")

