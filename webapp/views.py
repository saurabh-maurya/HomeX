from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ApplianceStatus 
from .serializers import ApplianceStatusSerializer, UserSerializer


from .models import *

class ApplianceStatusView(viewsets.ModelViewSet):
    queryset = ApplianceStatus.objects.all()
    serializer_class = ApplianceStatusSerializer
	
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserPutView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def loginpage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None :
            status = ApplianceStatus.objects.get(email_add=user.email)
            login(request,user)
            return redirect('home',uid=status.user_id)
    return render(request,'login/login.html',context=context)


@csrf_exempt
@login_required(login_url='login')
def homepage(request,uid):
    status = ApplianceStatus.objects.get(user_id=uid)
    if request.method == 'POST':
        change = ApplianceStatus(user_id=uid)
        change.f_name=status.f_name
        change.email_add=status.email_add
        change.fan = status.fan
        change.light = status.light
        change.motor = status.motor

        if 'onButtonFan' in request.POST:
            change.fan = 'ON'
        elif 'offButtonFan' in request.POST:
            change.fan = 'OFF'
        elif 'onButtonLight' in request.POST:
            change.light = 'ON'
        elif 'offButtonLight' in request.POST:
            change.light = 'OFF'
        elif 'onButtonMotor' in request.POST:
            change.motor = 'ON'
        elif 'offButtonMotor' in request.POST:
            change.motor = 'OFF'
        change.save()
        return redirect('home',uid=status.user_id)
    
    context={'status':status}
    return render(request,'home/index.html',context)

def logoutpage(request):
    logout(request)
    return redirect('login')