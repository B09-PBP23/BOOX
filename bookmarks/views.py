from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def show_bookmarks(request):
    user = request.user
    sorting = request.GET.get('sort', 'az') 
    bookmarked_books = Bookmarked.objects.filter(user=user).select_related('book')

    if sorting == 'za':
        bookmarked_books = bookmarked_books.order_by('-book__title')
    elif sorting == 'release_old':
        bookmarked_books = bookmarked_books.order_by('book__year')
    elif sorting == 'release_new':
        bookmarked_books = bookmarked_books.order_by('-book__year')
    elif sorting == 'modified':
        bookmarked_books = bookmarked_books.order_by('-bookmarked_at')

    response = {
        'bookmarked_books': bookmarked_books
    }
    return render(request, "bookmarks.html", response)


@login_required
def add_to_bookmark(request, book_id):
    if request.method == 'POST':
        user = request.user
        try:
            book = Books.objects.get(pk=book_id)
            # Check if the book is already bookmarked by the user
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
