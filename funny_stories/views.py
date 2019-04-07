from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from funny_stories.models import FunnyStories, FunStorTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def funny_main(request):
    all_funny_stories = FunnyStories.objects.all().order_by('created_date')
    page = request.GET.get("page", 1)
    paginator = Paginator(all_funny_stories, 9)
    stories_sorted = FunnyStories.objects.all().order_by('-views_count')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    return render(request, "funny_stories/funny_stories_main.html", {"funny_stories": all_funny_stories,
                                                                     "stories": stories,
                                                                     'stories_sorted': stories_sorted
                                                                     })


def fun_story(request, fun_story_pk):
    story = get_object_or_404(FunnyStories, pk=fun_story_pk)
    story.views_count += 1
    story.save()
    related_tags = story.tags.all()
    stories_sorted = FunnyStories.objects.all().order_by('-views_count')
    tags_list = []  # creating list of tags to lookup stories related to these tags
    for tag in related_tags:
        tags_list.append(tag.name)
    # "featured_stories" query returns 3 stories related to tags of current story with max nuber of views
    featured_stories = FunnyStories.objects.filter(tags__name__in=tags_list).order_by('views_count').exclude(
        name=story.name).distinct()[:2]
    return render(request, "funny_stories/funny_story_page.html", {"story": story, "related_tags": related_tags,
                                                                   'featured_stories': featured_stories,
                                                                   'stories_sorted': stories_sorted,
                                                                   })


def fun_tags(request, tag_pk):
    tag = get_object_or_404(FunStorTag, pk=tag_pk)
    related_stories = tag.funny_story.all().order_by('created_date')
    page = request.GET.get("page", 1)
    paginator = Paginator(related_stories, 9)
    stories_sorted = FunnyStories.objects.all().order_by('-views_count')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)
    return render(request, "funny_stories/funny_tags.html", {"tag": tag, "related_stories": related_stories,
                                                             "stories_sorted": stories_sorted, "stories": stories})
