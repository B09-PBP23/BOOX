import json
from django.db.models import F
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from landing_page.models import Books
from readers_favorite.models import ReadersFavorite, Comments
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum

def show_readers_favorite(request):
    books = Books.objects.all()

    if request.user.is_authenticated:
        user = request.user  # Get the current user
        all_comments = Comments.objects.all()
        user_contribution = Comments.objects.filter(user=user).count()

        # Try to get the user's existing ReadersFavorite or create a new one
        user_selected, created = ReadersFavorite.objects.get_or_create(user=user, user_contribution = user_contribution)

        response = {
            'books': books,
            'all_comments': all_comments,
        }
        return render(request, "readers_favorite.html", response)
    else:
        response = {
            'books': books,
        }
        return render(request, "readers_favorite_base.html", response)


def get_all_comments(request):
    data = Comments.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_commenters(request):
    data = ReadersFavorite.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def add_upvote_ajax(request, item_id):
    if request.method == 'POST':
        book_selected = get_object_or_404(Books, id=item_id)
        book_selected.total_upvotes += 1
        book_selected.save()
        # Return a JSON response to update the client-side data
        response_data = {'success': True}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponseNotFound()

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        user_comment = request.POST.get("user_comment")
        user = request.user
        new_comment = Comments(user=user, user_comment=user_comment)
        new_comment.save()

        # Increment user_contribution by 1 for the current user
        ReadersFavorite.objects.filter(user=user).update(user_contribution=F('user_contribution') + 1)

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()



