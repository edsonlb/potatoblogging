#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from blog.forms import PostForm
from blog.models import Post

def index(request):
    new_posts = Post.objects.filter(online=True).order_by('-date')[:3]
    old_posts = Post.objects.filter(online=True).order_by('-date')[3:]

    return render(request, 'index.html', {'old_posts': old_posts, 'new_posts': new_posts})

def newpost(request):
    form = PostForm()
    return render(request, 'postform.html', {'form': form, 'page_name': 'My new post'})

def newpost_save(request):
    if request.method == 'POST':
        try:
            post = Project.objects.get(id=request.POST.get('id','0'))   
            form = PostForm(request.POST, instance=post)  
        except:
            form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'postform.html', {'form': form})    
    else:
        return HttpResponseRedirect('/')
