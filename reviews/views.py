from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

from core.mixins import LoginOnlyView
from .models import Review
from books.models import Book
from movies.models import Movie

# Create your views here.
class ReviewCreateView(LoginOnlyView, SuccessMessageMixin, CreateView):
    model = Review
    extra_context = {
        "page_title": "Reviewing",
    }
    fields = ('text', 'rating',)
    template_name = "reviews/create_review.html"
    review_type = None
    obj_pk = None
    success_message = "Review created."

    def get_initial(self):
        super().get_initial()
        self.success_url = self.request.GET.get("next", reverse_lazy("core:home"))
        self.review_type = self.request.GET.get("type")
        self.obj_pk = self.kwargs.get("pk")
        
    
    def form_valid(self, form):
        print(self.review_type)
        if self.review_type is not None:
            obj = None
            is_movie = self.review_type == "movie" and True or False
            
            if is_movie:
                obj = Movie.objects.get(pk=self.obj_pk)
            else:
                obj = Book.objects.get(pk=self.obj_pk)

            if obj is not None:
                review = form.save(commit=False)
                review.created_by = self.request.user
                if is_movie:
                    review.movie = obj
                else:
                    review.book = obj
                return super().form_valid(form)
        else:
            return Http404()


@login_required
def delete_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
        next_url = request.GET.get("next")
        
        if review.created_by == request.user:
            review.delete()

        messages.add_message(request, messages.SUCCESS, "Review is deleted")
        if next_url is not None:
            return redirect(next_url)
        else:
            return redirect(reverse("core:home"))
    except Review.DoesNotExist:
        return redirect(reverse("core:home"))