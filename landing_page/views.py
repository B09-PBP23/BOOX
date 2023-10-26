from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import *

# Create your views here.
def get_books(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_landing_page(request):
    books = Books.objects.all()
    response = {
        'books':books
        }
    return render(request, "landing_page.html", response)

def get_data_json(request):
    product_item = Books.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))