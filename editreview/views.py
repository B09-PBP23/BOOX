from django.shortcuts import render

# Create your views here.
from django.core import serializers

from django.shortcuts import get_object_or_404, render, redirect
from landing_page.models import Books
from editreview.models import Review
from .forms import ReviewForm  # Diasumsikan Anda memiliki form untuk Review.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def editreview(request, id):
    # Get product berdasarkan ID
    
    review = Review.objects.get(pk = id, user = request.user)  #ini tuh buat apa ya, bener gasih BokkReview

    # Set product sebagai instance dari form
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:landing_page'))

    context = {'form': form,
               'review': review}
    return render(request, "editreview.html", context)
def get_review(request):
    data = Review.objects.all()
    context = {'reviews': data}
    
    return render(request, "editreview.html", context)
def display_reviews(request):
    # Ambil semua data reviews
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'display_reviews.html', context)

