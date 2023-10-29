from django.shortcuts import render

# Create your views here.
from django.core import serializers

from django.shortcuts import get_object_or_404, render, redirect
from landing_page.models import Books
from editreview.models import Review
from .forms import ReviewForm  # Diasumsikan Anda memiliki form untuk Review.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse

@login_required
def editreview(request, id):
    # Get product berdasarkan ID

    review = get_object_or_404(Review, pk=id, user=request.user)
    # Set product sebagai instance dari form
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('landing_page:show_landing_page'))

    context = {'form': form,
               'review': review}
    return render(request, "editreview.html", context)
def get_review(request):
    data = Review.objects.all()
    context = {'reviews': data}
    print(data)
    
    return render(request, "editreview.html", context)
def display_reviews(request):
    # Ambil semua data reviews
    
    reviews = Review.objects.all()
    print(reviews)
    context = {
        'reviews': reviews,
    }

    return render(request, 'display_reviews.html', context)
def get_books(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required
@require_http_methods(["POST"])
def edit_review_ajax(request):
    try:
        data = json.loads(request.body)
        review_id = data.get('id')
        review = get_object_or_404(Review, pk=review_id, user=request.user)
        form = ReviewForm(data, instance=review)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Review updated successfully.'})
        else:
            print(form.errors)  # Log form errors
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Exception as e:
        print(e)  # Log general errors
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
