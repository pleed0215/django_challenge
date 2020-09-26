from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy

from core.mixins import LoginOnlyView
from .models import Movie


class MoviesListView(ListView):
    model = Movie
    template_name = "movies/movies.html"
    paginator_class = Paginator
    paginate_by = 10
    ordering = "-year"
    context_object_name = "movies"
    extra_context = {"page_title": "Movies"}


class MovieDetailView(DetailView):
    template_name = "movies/movie_detail.html"
    model = Movie
    context_object_name = "movie"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["page_title"] = f"Movie: {self.get_object().title}"
        return context


class MovieCreateView(LoginOnlyView, SuccessMessageMixin, CreateView):
    model = Movie
    success_url = reverse_lazy("movies:movies")
    success_message = gettext_lazy("Movie data is successfully made.")
    template_name = "create_model.html"
    fields = [
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    ]
    extra_context = {
        "page_title": "Add Movie",
    }


class MovieUpdateView(LoginOnlyView, SuccessMessageMixin, UpdateView):
    model = Movie
    success_url = reverse_lazy("movies:movies")
    success_message = gettext_lazy("Movie data is successfully updated.")
    template_name = "create_model.html"
    fields = [
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    ]
    extra_context = {
        "page_title": "Update Movie",
    }
