from django.shortcuts import render
from landing_page.models import Books
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from add_review.forms import ReviewForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from editreview.models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
def add_review(request,book_id):
    book = Books.objects.filter(pk=book_id)
    form = ReviewForm(request.POST or None)

    book_instance = Books.objects.get(pk=book_id)
    form.instance.book = book_instance
    if form.is_valid() and request.method == "POST": 
        form.instance.user = request.user
        form.instance.book = book_instance
        form.save()
        return HttpResponseRedirect(reverse('add_review:show_review'))
    
    context = {'form':form,
               'book':book[0]}
    return render (request, "add_review.html", context)

def get_reviews(request, book_id):
    book = Books.objects.get(pk=book_id)
    data = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize("json", data))

@login_required(login_url='authentication:login')
def get_review_by_user(request, book_id):
    book = Books.objects.get(pk=book_id)
    data = Review.objects.filter(user=request.user, book=book)
    return HttpResponse(serializers.serialize("json", data))

@login_required(login_url='authentication:login')
def show_review(request, book_id):
    book = Books.objects.filter(pk=book_id)
    reviews = Review.objects.filter(book=book_id).order_by('-created_at')
    context = {
        'reviews':reviews,
        'user':request.user,
        'book':book[0]
        }
    return render(request, "show_review.html", context)

def get_username(request, book_id):
    book = Books.objects.get(pk=book_id)
    reviews = Review.objects.filter(book=book)
    usernames = [review.user.username for review in reviews]

    return JsonResponse({"fields": usernames})

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        book_pk = request.POST.get('book')
        book = Books.objects.get(pk=book_pk)
        if Review.objects.filter(user=request.user, book=book).exists():
            return HttpResponse(b"ALREADY EXISTS", status=200)
        
        user = request.user
        review = request.POST.get('review')
        rating = request.POST.get('rating')

        new_review = Review.objects.create(book=book, user=user, review=review, rating=rating)

        book.total_ratings += int(rating)
        book.total_reviews += 1

        print(book.total_ratings)
        book.save()
        new_review.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()