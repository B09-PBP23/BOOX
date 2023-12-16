import datetime
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
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

@login_required
def show_json(request):
    profile = get_object_or_404(Profile, user=request.user)
    serialized_data = serializers.serialize("json", [profile])
    return JsonResponse(serialized_data, safe=False)

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
        try:
            profile = Profile.objects.get(user=request.user)
            # Update the existing profile with new data
            profile.name = data.get("name", profile.name)
            profile.description = data.get("description", profile.description)
            profile.favorite_books = data.get("favoriteBooks", profile.favorite_books)
            profile.favorite_author = data.get("favoriteAuthor", profile.favorite_author)
            profile.save()
            return JsonResponse({"status": "success"}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "error", "message": "Profile not found"}, status=404)
    else:
        return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

@csrf_exempt
def create_profile_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_profile = Profile.objects.create(
            user = request.user,
            name = data["name"],
            description = data["description"],
            favorite_books = data["favoriteBooks"],
            favorite_author = data["favoriteAuthor"],
        )
        new_profile.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
