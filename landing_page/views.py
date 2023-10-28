from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.core import serializers
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_books(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_faq_data_json(request):
    data = FAQ.objects.all()
    print(data)
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

def get_faq_data(request):
    faq = FAQ.objects.all()
    return HttpResponse(serializers.serialize('json', faq))

@login_required(login_url='authentication:login')
def get_faq_data_per_user(request):
    faq = FAQ.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', faq))

@csrf_exempt
def add_faq_question(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        question = request.POST.get('question')
        is_public = bool(request.POST.get('is_public'))
        user = request.user

        if category and question:
            faq = FAQ.objects.create(user=user, category=category, question=question, is_public=is_public)
            faq.save()
            return HttpResponse(b'CREATED', status=201)
        else:
            return HttpResponseBadRequest('Invalid input. Please check your input again.')

    return HttpResponseNotFound()


def check_if_user_logged_in(request):
    if request.user.is_authenticated:
        return HttpResponse('true')
    else:
        return HttpResponse('false')

# @login_required(login_url='authentication:login')
# def get_review_data(request, book_id):
#     if request.method == 'GET':
#         book = get_object_or_404(Books, pk=book_id, user=request.user)
#         response = {
#             'book':book
#             }
#         return HttpResponse(serializers.serialize('json', [book]), content_type="application/json")
#     return HttpResponseNotFound()

# def show_review(request, book_id):
#     book = Books.objects.filter(pk=book_id)
#     response = {
#         'book':book[0]
#         }
#     return render(request, 'add_review.html', response)