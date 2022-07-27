from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    return HttpResponse("<h1> Home </h1>")

def about(request):
    return HttpResponse("<h1> About </h1>")

def register(request):
    return render(request=request, template_name="register.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="frontEnd/register.html", context={"register_form":form})
