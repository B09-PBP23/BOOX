import json
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from landing_page.models import Books
from readers_favorite.models import ReadersFavorite
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def show_readers_favorite(request):
    books = Books.objects.all()
    user_info = ReadersFavorite.objects.all()

    if request.user.is_authenticated:
        response = {
            'books': books,
            'user_info':user_info,
        }
        return render(request, "readers_favorite.html", response)
    else:
        response = {
            'books': books,
        }
        return render(request, "readers_favorite_base.html", response)


def get_user_info(request):
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
        new_comment = ReadersFavorite(user_comment=user_comment, user=user)
        new_comment.user_contribution += 1
        new_comment.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()



