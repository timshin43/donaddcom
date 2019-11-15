from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Blog_Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def blog_main(request):
    all_blog_post = Blog_Post.objects.all().order_by('-created_date')
    page = request.GET.get("page", 1)
    paginator = Paginator(all_blog_post, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/blog_main.html", {"all_blog_post": all_blog_post,
                                                              "posts": posts
                                                              })

def blog_post(request,blog_post_pk):
    post = get_object_or_404(Blog_Post, pk=blog_post_pk)
    post.views_count += 1
    post.save()
    return render(request, "blog/blog_page.html", {"post": post
                                                              })

