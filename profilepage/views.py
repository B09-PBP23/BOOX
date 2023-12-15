import json
from django.shortcuts import render, redirect
from profilepage.models import Profile
from .forms import UserProfileForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from landing_page.models import Books

@login_required(login_url='authentication:login')
def show_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        books = Books.objects.all()
        profiles = Profile.objects.filter(user=request.user)
        form = UserProfileForm(instance=profile)
        context = {
            'user_name': request.user.username,
            'profiles': profiles,
            'form':form,
        }
        return render(request, "profile.html", context)
    except Profile.DoesNotExist:
        return redirect('profilepage:create_profile')

@csrf_exempt
def create_profile(request):
    books = Books.objects.all()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profilepage:show_profile')
    else:
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = UserProfileForm(instance=profile)

    context = {'form': form,'books':books}
    return render(request, 'createprofile.html', context)


def get_profile_json(request):
    profiles = Profile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', profiles))

def show_json(request):
    data = Profile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def edit_profile_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        profile_picture = request.POST.get()
        user = request.user

        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = Profile(user=user)

        profile.name = name
        profile.description = description
        profile.profile_picture = profile_picture
        profile.save()

        return JsonResponse({'status': 'SUCCESS', 'message': 'Profile updated successfully'})
    
    return JsonResponse({'status': 'ERROR', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def edit_profile_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_profile = Profile.objects.get_or_create(
            user = request.user,
            name = data["name"],
            date_joined = data["date_joined"],
            description = data["description"],
            favorite_books = data["favorite_books"],
            favorite_author = data["favorite_author"],
        )
        new_profile.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

