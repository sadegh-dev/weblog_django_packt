from django.shortcuts import render, redirect
from .models import Post
from .forms import add_post_form

# Create your views here.


def page_index(request):
    #posts = Post.objects.all()
    posts = Post.objects.order_by('-release_datetime')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def page_add_post(request):
    if request.method == 'POST':
        form = add_post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = add_post_form()
        context={
            'form':form
        }
        return render(request, 'add-post.html', context)

