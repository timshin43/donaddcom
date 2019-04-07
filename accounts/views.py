from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .models import AppUser
from .forms import SignUpForm, MainUserForm, ProfileForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy


# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
			# uncomment if you need extra fields. See models
            # user.app_user.country = form.cleaned_data.get('country')
            # user.app_user.state = form.cleaned_data.get('state')
            # user.app_user.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            auth_login(request, user)
            return redirect('hom_page')
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': form})

# uncomment if you need extra fields. See models
def UserProfile(request):
    try:
        if request.method == 'POST':
            main_form = MainUserForm(request.POST, instance=request.user)
            # prof_form = ProfileForm(request.POST, instance=request.user.app_user)
            # if main_form.is_valid() and prof_form.is_valid():
            if main_form.is_valid():
                main_form.save()
                # prof_form.save()
                return redirect('my_account')
        else:
            main_form = MainUserForm(instance=request.user)
            # prof_form = ProfileForm(instance=request.user.app_user)
            # list_of_forms = [main_form, prof_form]
            list_of_forms = [main_form]
        return render(request, 'accounts/my_account.html', {'list_of_forms': list_of_forms})
    except:
        return redirect('login')


class UserUpdateView(UpdateView):
    model = AppUser
    # fields = ('first_name', 'last_name', 'email', )
    fields = ('country',)
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user.app_user
