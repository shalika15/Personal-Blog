from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.


def home(request):
    #import ipdb;
    #ipdb.set_trace()
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/home.html', {'posts': posts})


def post_details(request, post_id):
    #post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
    Post.objects.all()
