from django.shortcuts import render, redirect
from .models import *


def index(request):
	context = {
		"all_dojos": Dojo.objects.all()
	}
	return render(request,"index.html", context)

def create_dojo(request):
	print("REQUEST RECEIVED")
	new_dojo=Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
	return redirect('/')

def create_ninja(request):
	new_ninja=Ninja.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], dojo= Dojo.objects.get(id=request.POST['dojo_id']))
	return redirect('/')




# Create your views here.
