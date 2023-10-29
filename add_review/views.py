from django.shortcuts import render
from landing_page.models import Books
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from add_review.forms import ReviewForm
from django.urls import reverse
# Create your views here.

# def add_review(request,book_id):
   
#     try:
#         book = Books.objects.filter(pk=book_id)
#         print("Book fetched:", book)
#     except Books.DoesNotExist:
#         print(f"No book found")
#         return HttpResponseNotFound("Book not found")

#     form = ReviewForm(request.POST or None)
#     if form.is_valid() and request.method == "POST": 
#         form.save()
#         return HttpResponseRedirect(reverse('landing_page:show_review'))
    
#     context = {'form':form,
#                'book':book}
#     return render (request, "add_review.html", context)

def add_review(request,book_id):
    book = Books.objects.filter(pk=book_id)
    form = ReviewForm(request.POST or None)

    book_instance = Books.objects.get(pk=book_id)
    form.instance.book = book_instance
    if form.is_valid() and request.method == "POST": 
        form.instance.user = request.user
        form.instance.book = book_instance
        form.save()
        return HttpResponseRedirect(reverse('landing_page:show_review'))
    
    context = {'form':form,
               'book':book[0]}
    return render (request, "add_review.html", context)

def get_books(request): 
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

