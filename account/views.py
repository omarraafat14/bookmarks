from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # checks user credentials and returns a User object if they are correct;
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # sets the user in the current session.
                    login(request, user)
                    return HttpResponse("You are now logged in as %s" % username)
                else:
                    return HttpResponse("This account is disabled")
            else:
                return HttpResponse("Invalid username and/or password")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})
