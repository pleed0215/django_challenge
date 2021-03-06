from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.translation import gettext_lazy

from core.mixins import LoginOnlyView
from .models import Person


class PeopleListView(ListView):
    model = Person
    template_name = "people/people.html"
    paginator_class = Paginator
    paginate_by = 10
    ordering = "-created_at"
    context_object_name = "people"
    extra_context = {"page_title": "People"}


class PersonDetailView(DetailView):
    template_name = "people/person_detail.html"
    model = Person
    context_object_name = "person"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["page_title"] = f"Person: {self.get_object().name}"
        return context


class PersonCreateView(LoginOnlyView, SuccessMessageMixin, CreateView):
    model = Person
    success_url = reverse_lazy("people:people")
    success_message = gettext_lazy("Person data is successfully made.")
    template_name = "create_model.html"
    fields = [
        "name",
        "photo",
        "kind",
    ]
    extra_context = {
        "page_title": "Add Person",
    }


class PersonUpdateView(LoginOnlyView, SuccessMessageMixin, UpdateView):
    model = Person
    success_url = reverse_lazy("books:books")
    template_name = "create_model.html"
    success_message = gettext_lazy("Person data is successfully updated.")
    fields = [
        "name",
        "kind",
        "photo",
    ]
    extra_context = {
        "page_title": "Update Person",
    }
