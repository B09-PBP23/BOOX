from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from .models import BookReview
from .forms import ReviewForm  # Diasumsikan Anda memiliki form untuk Review.
from django.http import HttpResponseRedirect
from django.urls import reverse

# def edit_review(request, review_id):
#     review = get_object_or_404(Review, id=review_id, user=request.user)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             form.save()
#             return redirect('some_view_name')  # Gantikan 'some_view_name' dengan nama view tujuan setelah menyimpan.
#     else:
#         form = ReviewForm(instance=review)
#     return render(request, 'editreview.html', {'form': form})
def editreview(request, id):
    # Get product berdasarkan ID
    review = BookReview.objects.get(pk = id)  #ini tuh buat apa ya, bener gasih BokkReview

    # Set product sebagai instance dari form
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "editreview.html", context)