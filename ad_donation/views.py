from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ad_donation.models import Total_donation, Video, Donations, Project_for_donations
from random import randint, sample
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
import random


# Create your views here.
@login_required
def ad_donation(request):
    # user_auth = request.user.is_authenticated
    count = Video.objects.all().count()
    all_objects = Video.objects.all()
    ids_list = Video.objects.all().values_list('pk', flat=True).order_by("pk")
    rand_id = random.choice(ids_list)
    video = Video.objects.get(pk=rand_id)
    return render(request, "ad_donation/ad_don_main.html", {"video": video, "count": count, })

@ensure_csrf_cookie
@login_required
def donate(request,donat_project_pk):
	donation_user = Donations(amount=0.15, who_donated=request.user)
	donation_user.save()
	donation_project = get_object_or_404(Project_for_donations, pk=donat_project_pk)
	donation_user.project.add(donation_project)
	video = get_object_or_404(Video,pk=request.GET['video_pk'])
	video.views_count += 1
	video.save()
	# all_donation_user = Donations.objects.all()
	# don_from_users = 0
	# for don in all_donation_user:
		# don_from_users = don_from_users + don.amount
		
	project_donations = round(sum(donation_project.project_donation.all().values_list('amount',flat=True).order_by("pk")),2)
	donation_project.amount_donated = project_donations

	if(donation_project.amount_required !=0):
		project_progress = round(project_donations/donation_project.amount_required*100,1)
	else:
		project_progress = 0
		
	donation_left = donation_project.amount_required-project_donations
	donation_project.amount_donated = project_donations	
	donation_project.percentage_donated = project_progress	
	donation_project.save()
	data = { "don_from_users": round(donation_left,2),"project_progress":project_progress,"project_donations":project_donations }
	# return redirect('add_donation')
	return JsonResponse(data)




def donate_test(request):
    data_from_page = "fgdf"
    return HttpResponse(data_from_page)
	
def donate_main(request):
	all_projects = Project_for_donations.objects.all().order_by('created_date')
	return render(request, "ad_donation/ad_don_main.html", {"all_projects": all_projects,
																	 })
																	 
def donate_project(request,donat_project_pk):
	project = get_object_or_404(Project_for_donations, pk=donat_project_pk)
	current_lang = request.LANGUAGE_CODE
	try:
		ids_list = project.project_video.filter(language=current_lang).values_list('pk',flat=True).order_by("pk")
		rand_id = random.choice(ids_list)
		video = project.project_video.get(pk=rand_id)
	except:
		video= get_object_or_404(Video,name="emergency_video") # we need this block if we cannot find video corresponding to our project above
	project_donations = sum(project.project_donation.all().values_list('amount',flat=True).order_by("pk"))
	if(project.amount_required !=0):
		project_progress = round(project_donations/project.amount_required*100,1)
	else:
		project_progress = 0
	return render(request, "ad_donation/donation_project_detail.html", {"project": project, "video":video,
																		"project_progress":project_progress,
																		"amount_required":round(project.amount_required,2),
																		"project_donations":round(project_donations,2)
																	 })


def success_main(request):
    all_success_stories = Success_stories.objects.all().order_by('created_date')
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