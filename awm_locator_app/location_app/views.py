from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


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