import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.gis.geos import Point
from django.http import JsonResponse
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


@login_required
def update_location(request):
    try:
        profile = request.user.userprofile

        if not profile:
            raise ValueError("Can't get user profile")

        location = json.loads(request.body)

        profile.test_location = location
        lat = float(location['latitude'])
        long = float(location['longitude'])

        profile.latitude = lat
        profile.longitude = long
        profile.user_location = Point(lat, long, srid=4326)
        profile.save()

        return JsonResponse(f"Location updated to {lat}, {long}", status=200, safe=False)
    except Exception as e:
        return JsonResponse("Error: " + str(e), status=400, safe=False)



