from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'main.html', context)

def admin_page(request):
    posts=Post.objects.all()
    context={
        'posts': posts    
    }
    return render(request, 'admin.html', context)

def upload_image(request): #new
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(admin_page)
    else:
        form = PostForm()
        context = {
            'form': form
        }
    return render(request, 'new.html', context)

def edit_message(request, pk):
    # Retrieve the object containing the message
    message = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            return redirect('admin')  # Redirect to success URL after editing
    else:
        form = PostForm(instance=message)
    
    return render(request, 'update.html', {'form': form})

def delete_message(request, pk):
    message = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('admin')  # Redirect to success URL after deletion
    return render(request, 'delete.html', {'message': message})