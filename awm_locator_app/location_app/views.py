from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import UserProfile
from location_app.forms import RegisterUserForm


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("/menu")
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        form = AuthenticationForm()
        return render(request=request, template_name="user_forms/login.html", context={"login_form": form})


def new_user_registration(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            username = request.POST.get('username')
            email = request.POST.get('email')
            form.save()
            new_profile = UserProfile(user=new_user, username=username, email=email)
            new_profile.save()
            return redirect("/register_success")
        else:
            return redirect("/")
    else:
        form = RegisterUserForm()
    return render(request=request, template_name="user_forms/register.html", context={"signup_form": form})


def user_logout(request):
    logout(request)
    return redirect("/")

