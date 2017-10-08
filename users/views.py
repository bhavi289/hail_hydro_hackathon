from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from .models import Users, Plants, Vehicles, Members
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
userid = -1
def homepage(request):
	return render(request, 'users/index.html')

def loginpage(request):
	return render(request, 'users/login.html')

def temperature(request):
	return render(request, 'users/index.html')

def signUp(request):
	if request.POST:
		t = Users(name=request.POST['name'],password=request.POST['password'],phone=request.POST['username'],address=request.POST['address'])
		t.save()		
		return redirect('../login')
	return render(request, 'users/loginpage.html')

def login(request):
	r = False
	if request.POST:
		t = Users.objects.filter(password=request.POST['password'],phone=request.POST['username'])
		if len(t):
			request.session['name'] = t[0].name
			request.session['id'] = t[0].id
			global userid
			userid = t[0].id
			return redirect('../../sensors/data')
		else:
			messages.error(request, 'no such user')
			return render(request, 'users/login.html')
	return render(request, 'users/login.html',{"r":r})

def addplant(request):
	r = False
	if request.POST:
		global userid
		uid = userid
		z = get_object_or_404(Users, pk=userid)
		print("hello")
		f = Plants.objects.filter(userid = z)
		if f:
			p = Plants(userid = z, plantName = request.POST['plantname'])
			p.save()
			print("not")
		else:
			p = Plants(userid = z, plantName = request.POST['plantname'])
			p.save()
			z.currentplant = p.id
			z.save()
			print("now")
		z = Plants.objects.filter(userid = userid)
		print(z)
		return redirect('../../sensors/data')
	return render(request, 'users/addplant.html')

def addVehicle(request):
	if request.POST:
		global userid
		z = get_object_or_404(Users, pk=userid)
		print("hello")
		v = Vehicles(userid = z, vehicle = request.POST['vehiclename'])
		v.save()
		z.vehicleCount += 1
		z.save()
		return redirect('../../sensors/data')
	return render(request, 'users/addVehicle.html')

def addMember(request):
	if request.POST:
		global userid
		z = get_object_or_404(Users, pk=userid)
		print("hello")
		v = Members(userid = z, memberName = request.POST['membername'])
		v.save()
		z.membercount += 1
		z.save()
		return redirect('../../sensors/data')
	return render(request, 'users/addMember.html')



# ----------------- API --------------------

@csrf_exempt
def mobile_login(request):
	if request.method=='POST':
		jsonResponse=json.loads(request.body.decode('utf-8'))
		username=jsonResponse['json_data']['username']
		password=jsonResponse['json_data']['password']
		print(password)
		t = Users.objects.filter(password=password,phone=username)

		if len(t):
			#request.session['name'] = t[0].name
			#request.session['id'] = t[0].id

			global userid
			userid = t[0].id
			u={"pass":"true","id":t[0].id,"name":t[0].name,"phone":t[0].phone,"address":t[0].address,"currentplant":t[0].currentplant,"vehicleCount":t[0].vehicleCount,"membercount":t[0].membercount}
			return JsonResponse(u)
		else:
			u={"pass":"false"}
			return JsonResponse(u)