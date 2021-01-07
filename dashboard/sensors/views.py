from django.contrib.auth import authenticate, login,logout
# from visual.models
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.http import Http404
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from random import randint
import datetime
from dateutil import tz
import utilities
import time 
import json

# Create your views here.
def loginPage(request):
    return render(request, 'visual/login.html', None)

class authenticateLogin(APIView):
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user = authenticate(request, username=username, password=password)  

        if user is not None:
            login(request,user)
            return Response({"success":True})
        else:
            return Response({"success":False})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'sensors/dashboard.html', None)
    else:
        return HttpResponseRedirect(reverse('sensors:loginPage', args=()))


class macList(request):
    def get(self,request):
        pass

# API to fetch and post the sensors Data #
class sensorData(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            pass

    def post(self,request):
        macAddr = request.data.get('macaddress')
        



