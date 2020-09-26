from django.views.generic import ListView, DetailView

from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = "genres/genres.html"
    ordering = "name"
    context_object_name = "categories"
    extra_context = {"page_title": "Genres"}


class CategoryDetailView(DetailView):
    template_name = "genres/genre_detail.html"
    model = Category
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["page_title"] = f"Genre: {self.get_object().name}"
        return context
