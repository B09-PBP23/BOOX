import json
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from landing_page.models import Books
# from readers_favorite.models import ReadersFavorite
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def show_readers_favorite(request):
    books = Books.objects.all()
    response = {
        'books':books,
        }
    return render(request, "readers_favorite.html", response)

# def get_book_info(request):
#     data = Books.objects.all()
#     return HttpResponse(serializers.serialize('json', data))

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





