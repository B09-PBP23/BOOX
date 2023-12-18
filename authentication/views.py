import datetime  

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
import json

# Create your views here.
@csrf_exempt
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')

        else:
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Account with this username already exists. Please choose a different username.')
            else:
                messages.error(request, 'Failed to create your account. Please correct the errors below.')

    context = {'form': form}
    return render(request, 'register.html', context)

<<<<<<< HEAD
<<<<<<< HEAD
@csrf_exempt
=======

>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
=======

>>>>>>> 439082c7645e65b3e365cf5c45e76b847d95f394
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("profilepage:show_profile"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('landing_page:show_landing_page'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def flutter_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login success!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed. Your account is inactive."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to login. Please check your username and password."
        }, status=401)

@csrf_exempt
def flutter_logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout success."
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout failed."
        }, status=401)
    
@csrf_exempt
def flutter_register(request):
    try:
        data = json.loads(request.body)

        username = data["username"]
        password1 = data["password1"]
        password2 = data["password2"]

        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Password did not match.'})

        new_user = User.objects.create_user(username = username, password = password1)
        new_user.save()
        return JsonResponse({"status": "success"}, status=200)
    except IntegrityError:
        return JsonResponse({"status": "error", 'message':'Username already exists.'}, status=401)
    except:
        return JsonResponse({"status": "error", 'message':'Error happened, please try again.'}, status=401)