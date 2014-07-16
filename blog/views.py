#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from blog.forms import PostForm
from blog.models import Post
from django.db.models import Q
import markdown

def index(request):
    new_posts = Post.objects.filter(online=True).order_by('-date')[:3]
    old_posts = Post.objects.filter(online=True).order_by('-date')[3:]

    return render(request, 'index.html', {'old_posts': old_posts, 'new_posts': new_posts})

def post(request):
    form = PostForm()
    return render(request, 'postform.html', {'form': form, 'page_name': 'My new post'})

def post_save(request):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=request.POST.get('id','0'))   
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

def post_view(request, postName):
    postName = postName.replace('_',' ')

    try:
        post = Post.objects.get(title=postName)
    except:
        return HttpResponseRedirect('/')

    return render(request, 'postview.html', {'post': post})

def post_delete(request, id):
    try:
        post = Post.objects.get(pk=id)
        post.delete()
    except:
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')

def post_edit(request, id):
    try:
        post = Post.objects.get(pk=id)   
        form = PostForm(instance=post)  
    except:
        HttpResponseRedirect('/')
        
    return render(request, 'postform.html', {'form': form})   

def post_search(request):
    if request.method == 'POST':
        search = request.POST.get('search','').strip()
        new_posts = Post.objects.filter(online=True).filter(Q(title__icontains=search) | Q(text__icontains=search)).order_by('-date')[:3]
        old_posts = Post.objects.filter(online=True).filter(Q(title__icontains=search) | Q(text__icontains=search)).order_by('-date')[3:]   

        return render(request, 'index.html', {'old_posts': old_posts, 'new_posts': new_posts})    
    else:
        return HttpResponseRedirect('/')

def post_offline(request):
    new_posts = Post.objects.filter(online=False).order_by('-date')[:3]
    old_posts = Post.objects.filter(online=False).order_by('-date')[3:]   

    return render(request, 'index.html', {'old_posts': old_posts, 'new_posts': new_posts})    