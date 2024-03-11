from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms
from .forms import SignUpForm


# register_user view handles both POST and GET requests.
def register_user(request):
    # if request is POST and form is valid, it saves the new user and log's in.
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  extract the username and text field from the data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # authenticate and login
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "You have successfully registered!")
            return redirect("home")
    # if form is invalid or request is GET (not POST),
    # it renders register.html template with form
    else:
        form = SignUpForm()
    return render(request, "registration/register.html", {"form": form})
