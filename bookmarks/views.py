from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from landing_page.models import Books

def landing_page(request):
    books = Books.objects.all()
    return render(request, 'landing_page.html', {'books': books})

def get_books(request):
    data = Bookmarked.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required
def show_bookmarks(request):
    user = request.user
    sorting = request.GET.get('sort', 'az') 
    bookmarked_books = Bookmarked.objects.all()
    # # sort by aphabetical, release date buku, dan tanggal di bookmark.
    # if sorting == 'za':
    #     bookmarked_books = bookmarked_books.order_by('-book__title')
    # elif sorting == 'release_old':
    #     bookmarked_books = bookmarked_books.order_by('book__year')
    # elif sorting == 'release_new':
    #     bookmarked_books = bookmarked_books.order_by('-book__year')
    # elif sorting == 'modified':
    #     bookmarked_books = bookmarked_books.order_by('-bookmarked_at')

    response = {
        'bookmarked_books': bookmarked_books
    }
    return render(request, "bookmarks.html", response)

def make_bookmarks(request):
    books = Book.object.all()

    if request.user.is_authenticated:
        user = request.user
        user_selected, created = bookmarks.objects.get_or_create(user=user)

        response = {
            'books': books,
        }
        return JsonResponse(response) # jika user terautentikasi
    else: 
        return JsonResponse({'message: User not authenticated'})

@login_required
def add_to_bookmark(request, book_id):
    if request.method == 'POST':
        user = request.user
        try:
            book = Books.objects.get(pk=book_id)
            if not Bookmarked.objects.filter(user=user, book=book).exists():
                bookmark = Bookmarked(user=user, book=book)
                bookmark.save()
                return JsonResponse({'message': 'Bookmarked successfully'}, status=200)
            else:
                return JsonResponse({'message': 'Book is already bookmarked'}, status=400)
        except Books.DoesNotExist:
            return JsonResponse({'message': 'Book not found'}, status=400)
    return JsonResponse({'message': 'Invalid request'}, status=400)

@login_required
def remove_from_bookmark(request, book_id):
    if request.method == 'POST':
        user = request.user
        try:
            book = Books.objects.get(pk=book_id)
            bookmark = Bookmarked.objects.filter(user=user, book=book).first()
            if bookmark:
                bookmark.delete()
                return JsonResponse({'message': 'Removed from bookmarks successfully'}, status=200)
            else:
                return JsonResponse({'message': 'Book is not bookmarked'}, status=400)
        except Books.DoesNotExist:
            return JsonResponse({'message': 'Book not found'}, status=400)
    return JsonResponse({'message': 'Invalid request'}, status=400)
