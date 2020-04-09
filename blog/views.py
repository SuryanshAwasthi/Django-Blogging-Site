
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404



def post_home(request):
   post=Post.objects.all()
   return render(request, 'blog.html', {'post':post})


def post_detail(request, pk):
   post = get_object_or_404(Post, pk=pk)
   Post.objects.get(pk=pk)
   return render(request, 'blog_post.html', {'post': post})

def post_new(request):
   if request.method == "POST":
      form = PostForm(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user
         post.published_date = timezone.now()
         post.save()
         return redirect('post_edit.html', pk=post.pk)
   else:
      form = PostForm()
   return render(request, 'post_edit.html', {'form': form})