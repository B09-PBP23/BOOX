from django.shortcuts import render

def show_profile(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "profile.html", context)