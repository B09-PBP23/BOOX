from django.shortcuts import render

# Create your views here.
from django.core import serializers

from django.shortcuts import get_object_or_404, render, redirect
from landing_page.models import Books
from editreview.models import Review
from .forms import ReviewForm 
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def editreview(request, id):
    review = get_object_or_404(Review, pk=id, user=request.user)
    book = Books.objects.get(pk=review.book.pk)
    book.total_ratings -= int(review.rating)
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        form.save()
        book.save()
        return HttpResponseRedirect(reverse('landing_page:show_landing_page'), status=302)

    book.total_ratings += int(review.rating)
    context = {'form': form,
               'review': review
               }
    
    return render(request, "editreview.html", context)

def get_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    book = Books.objects.get(pk=review.book.id)
    context = {
        'review': review,
        'book': book
    }
    
    return render(request, "editreview.html", context)


def display_reviews(request):
    reviews = Review.objects.all()
    print(reviews)
    context = {
        'reviews': reviews,
    }

    return render(request, 'display_reviews.html', context)
def get_books(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")