from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.utils import timezone

# Create your models here.

# AppUser is a new model which allows to keep extra fields about users
STATES_CHOICE = (
    ('NAN', 'Not From States'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)


class AppUser(models.Model):
	#all fields below remained from the previous business logic. Now we do not need them but let them be just in case
    user = models.OneToOneField(User, related_name='app_user', on_delete=models.CASCADE)
    country = CountryField(blank=True)
    view_count=models.PositiveIntegerField(default=0)
    view_count_expire = models.DateTimeField(blank=True, default=timezone.now())
    state = models.CharField(max_length=25, choices=STATES_CHOICE, blank=True, default='NAN')
    birth_date = models.DateTimeField(blank=True, default=timezone.now())
    is_advertiser = models.BooleanField(blank=True, default=False)



# it is required to create AppUser instance instead of default User Model when we use standard
# Django`s users creation functionality
@receiver(post_save, sender=User)  # we use this function to connect user creation with AppUser creation
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        AppUser.objects.create(user=instance)


# it is required to create AppUser instance instead of default User Model when we use standard
# Django`s users creation functionality
@receiver(post_save, sender=User)  # we use this function to connect user creation with AppUser creation
def save_user_profile(sender, instance, **kwargs):
    instance.app_user.save()
