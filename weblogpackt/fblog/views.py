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




# ############## #
# codes in shell #
# ############## #
"""
from fblog.models import Post

# ADD new data in database
>>>> obj = Post(context="new context from shell", count_viewer=200)
>>>> obj.save()

# SELECT data from database
>>>> obj = Post.objects.get(count_viewer=100)
#OR
>>>> obj = Post.objects.get(id=2)
>>>> obj = Post.objects.get(pk=2)  // same code top
#if not exist send error


# SELECT All data from database
>>>> list_obj = Post.objects.all()
# list_obj [0..9] [id, context, count_viewer, ...]

# access all data
>>>> for a in list_obj :
>>>>    print(a.context)


>>>> the_obj = list_obj[0]
>>>> the_obj[context] = "update context from shell, hello"
# an save one field data
>>>> the_obj.save()



# UPDATE data in database
>>>> obj.context = "update context in database"

# DELETE data from database
>>>> obj.delete()

"""


