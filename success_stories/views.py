from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from success_stories.models import Success_stories, Tags
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def success_main(request):
    all_success_stories = Success_stories.objects.all().order_by('-created_date')
    page = request.GET.get("page", 1)
    paginator = Paginator(all_success_stories, 9)
    stories_sorted = Success_stories.objects.all().order_by('-views_count')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    return render(request, "success_stories/success_stories_main.html", {"success_stories": all_success_stories,
                                                                         "stories": stories,
                                                                         'stories_sorted':stories_sorted
                                                                         })


def s_story(request, s_story_pk):
    story = get_object_or_404(Success_stories, pk=s_story_pk)
    story.views_count += 1
    story.save()
    related_tags = story.tags.all()
    stories_sorted = Success_stories.objects.all().order_by('-views_count')
    tags_list = []  # creating list of tags to lookup stories related to these tags
    for tag in related_tags:
        tags_list.append(tag.name)
    # "featured_stories" query returns 3 stories related to tags of current story with max nuber of views
    featured_stories = Success_stories.objects.filter(tags__name__in=tags_list).order_by('views_count').exclude(name=story.name).distinct()[:2]
    return render(request, "success_stories/success_story_page.html", {"story": story, "related_tags": related_tags,
                                                                       'featured_stories': featured_stories,
                                                                       'stories_sorted':stories_sorted,
                                                                       })


def tags(request, tag_pk):
    tag = get_object_or_404(Tags, pk=tag_pk)
    related_stories = tag.success_story.all().order_by('created_date')
    page = request.GET.get("page", 1)
    paginator = Paginator(related_stories, 9)
    stories_sorted = Success_stories.objects.all().order_by('-views_count')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)
    return render(request, "success_stories/tags.html", {"tag": tag, "related_stories": related_stories,
                                                         "stories_sorted": stories_sorted, "stories": stories,})

