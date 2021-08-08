#from django.shortcuts import render

# Create your views here.
#def index(request):
  #  return render(request, 'index.html',)
from django.shortcuts import render, get_object_or_404

from .models import Post, PostImage


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog.html',{'posts':posts})

def portfolio_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'portfolio.html', {
        'post':post,
        'photos':photos
    })
