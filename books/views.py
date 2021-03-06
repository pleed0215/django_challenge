from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy

from core.mixins import LoginOnlyView
from .models import Book


class BooksListView(ListView):
    model = Book
    template_name = "books/books.html"
    paginator_class = Paginator
    paginate_by = 10
    ordering = "-year"
    context_object_name = "books"
    extra_context = {"page_title": "Books"}


class BookDetailView(DetailView):
    template_name = "books/book_detail.html"
    model = Book
    context_object_name = "book"
    extra_context = {
        "page_title": "Book Detail",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["page_title"] = f"Book: {self.get_object().title}"
        return context


class BookCreateView(LoginOnlyView, SuccessMessageMixin, CreateView):
    model = Book
    success_message = gettext_lazy("Book data is successfully made")
    success_url = reverse_lazy("books:books")
    template_name = "create_model.html"
    fields = [
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "writer",
    ]
    extra_context = {
        "page_title": "Add Book",
    }


class BookUpdateView(LoginOnlyView, SuccessMessageMixin, UpdateView):
    model = Book
    success_url = reverse_lazy("books:books")
    success_message = gettext_lazy("Book data is successfully updated")
    template_name = "create_model.html"
    fields = [
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "writer",
    ]
    extra_context = {
        "page_title": "Update Book",
    }
