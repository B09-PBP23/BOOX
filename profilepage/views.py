from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication:login')
def show_profile(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "profile.html", context)