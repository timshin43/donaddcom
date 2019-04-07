from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AppUser
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from django.forms import extras

# class SignUpForm(UserCreationForm):
# # email = forms.CharField(max_length=254, required=False, widget=forms.EmailInput())
# class Meta:
# model = User
# fields = ('username', 'password1', 'password2')

# class UserForm(forms.ModelForm):
# class Meta:
# model = User
# fields = ('first_name','last_name')

# class ProfileForm(forms.ModelForm):
# class Meta:
# model = AppUser
# fields = ('department', )
# we manually list all possible states
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

YEARS = [x for x in range(1940, 2018)]


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
	#uncomment if you need this fields for signing up. Also See models
    # CHOICES = (('America', 'USA'), ('RUS', 'Russia'),)
    # country = CountryField().formfield()
    # state = forms.ChoiceField(choices=STATES_CHOICE, required=False)
    # birth_date = forms.DateField(widget=extras.SelectDateWidget(years=YEARS))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class MainUserForm(forms.ModelForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email')

# this model is required to handle with this extra fields. No we not use this form since do not use this fields
class ProfileForm(forms.ModelForm):
    CHOICES = (('America', 'USA'), ('RUS', 'Russia'),)
    country = CountryField().formfield()
    state = forms.ChoiceField(choices=STATES_CHOICE, required=False)
    birth_date = forms.DateField(widget=extras.SelectDateWidget(years=YEARS))

    class Meta:
        model = AppUser
        fields = ('country', 'state', 'birth_date')
