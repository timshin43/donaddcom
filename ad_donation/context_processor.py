from .models import Total_donation, Donations
from django.utils import  translation


# we use context processor to have an access to course list from any html templates
def total_donation(request):
	all_donation_user = Donations.objects.all()
	don_from_users = 0
	# lang = django.utils.i18n.get_language
	lang = translation.get_language()
	for don in all_donation_user:
		don_from_users = don_from_users + don.amount
	return {
		#'total_donation': Total_donation.objects.get(name="main_total_donation"),
		'total_don_from_users': round(don_from_users, 2),
		'lang':lang
	}