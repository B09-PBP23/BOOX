from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import *
from django.contrib.auth.decorators import login_required
# from add_review.models import BookReviews

# Create your views here.
def get_books(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='auth/login')
def show_landing_page(request):
    books = Books.objects.all()
    response = {
        'books':books
        }
    return render(request, "landing_page.html", response)

def get_data_json(request):
    product_item = Books.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def get_review_data(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Books, pk=book_id)
        # reviews = BookReview.objects.filter(book=book)
        response = {
            'book':book
            }
        return HttpResponse(serializers.serialize('json', [book]), content_type="application/json")
    return HttpResponseNotFound()

def show_review(request, book_id):
    book = Books.objects.get(pk=book_id)
    response = {
        'book':book
        }
    return render(request, 'book_review.html', response)