from django.shortcuts import render

# Create your views here.
from django.core import serializers
import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from landing_page.models import Books
from editreview.models import Reply, Review
from .forms import ReviewForm  # Diasumsikan Anda memiliki form untuk Review.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def editreview(request, id):
    # Get product berdasarkan ID
    review = get_object_or_404(Review, pk=id, user=request.user)
    book = Books.objects.get(pk=review.book.pk)
    book.total_ratings -= int(review.rating)
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        book.save()
        return HttpResponseRedirect(reverse('landing_page:show_landing_page'))

    book.total_ratings += int(review.rating)
    context = {'form': form,
               'review': review
               }
    return render(request, "editreview.html", context)

def get_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    book = Books.objects.get(pk=review.book.id)
    context = {
        'review': review,
        'book': book
    }
    
    return render(request, "editreview.html", context)


def display_reviews(request):
    # Ambil semua data reviews
    
    reviews = Review.objects.all()
    print(reviews)
    context = {
        'reviews': reviews,
    }
    return render(request, 'display_reviews.html', context)
def get_books(request):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def editreviewflutter(request):
    if request.method == "POST":
        review_id = request.POST.get('id')
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')
        
        get_review = get_object_or_404(Review, pk=review_id, user=request.user)
        
        book = get_review.book
        book.total_ratings -= int(get_review.rating)
        book.total_ratings += int(rating)
        
        get_review.review = review_text
        get_review.rating = rating
        
        get_review.save()
        book.save()
        return JsonResponse({'status': 'success', 'id': get_review.pk, 'review': get_review.review, 'rating': get_review.rating})
    else:
        return HttpResponseBadRequest("Invalid request method.")
    
    
@csrf_exempt
def add_reply(request, user_name):
    if request.method == "POST":
        review_id = request.POST.get('id')
        reply = request.POST.get('reply')

        # Ensure a valid User instance

        new_reply = Reply.objects.create(user = Reply.objects.get(user=id), review=get_review, reply=reply)
        new_reply.save()

        # Optional: Update some user statistics here, similar to your friend's code

        return JsonResponse({'status': 'success', 'id': get_review.pk, "reply": reply})
    else:
        return HttpResponseBadRequest("Invalid request method.")

    

@csrf_exempt
def delete_reply_flutter(request, idReply):
    if request.method == 'DELETE':
        try:
            user_name = request.POST.get('username')
            user = User.objects.get(username=user_name)

            reply = Reply.objects.get(pk=idReply, user=user)
            reply.delete()

            return JsonResponse({"status": "success"}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"status": "error", "message": "User not found"}, status=404)
        except Reply.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Reply not found"}, status=404)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

def get_reply(request, idReview):
    data = Reply.objects.filter(review=idReview)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required
def edit_review_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            review_id = data.get('id')

            try:
                review = Review.objects.get(pk=review_id, user=request.user)
            except Review.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Review not found'}, status=404)

            form = ReviewForm(data, instance=review)

            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'success', 'message': 'Review updated successfully.'})
            else:
                print(form.errors)  # Log form errors
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

        except Exception as e:
            print(e)  # Log general errors
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
