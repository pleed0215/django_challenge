from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    views as auth_views,
    forms as auth_forms,
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import translation
from django.conf import settings

from core.mixins import LoginOnlyView, LoggedOutOnlyView
from . import forms
from .models import User


# Create your views here.
class LoginView(LoggedOutOnlyView, SuccessMessageMixin, auth_views.LoginView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    extra_context = {
      "page_title": "Log in"
    }
    success_message = "Login success"


    def form_valid(self, form):
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")

      user = authenticate(self.request, username=username, password=password)
      if user is not None:  
        login(self.request, user)
        return super().form_valid(form)
      else:
          print("login failed")
      return redirect(self.get_success_url())

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")

class SignupView(LoggedOutOnlyView, SuccessMessageMixin, FormView):
    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("core:home")
    success_message = "Congratulation! Welcome!"

    def form_valid(self, form):
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password1")

      form.save()
      user = authenticate(self.request, username=username, password=password)
      if user is not None:
          login(self.request, user)
      return redirect(self.get_success_url())


@login_required
def logout_view(request):
    messages.add_message(request, messages.SUCCESS, f"Byebye, {request.user}")
    logout(request)
    return redirect(reverse("core:home"))


class UserDetailView(LoginOnlyView, DetailView):
  class Meta:
    model = User
    fields = (
      "username",
      "bio",
      "email",
      "preference",
      "language",
      "fav_book_cat",
      "fav_movie_cat",
    )
  def get_object(self, queryset=None):
    return self.request.user

  template_name = "users/profile.html"


class UpdateProfileView(LoginOnlyView, SuccessMessageMixin, UpdateView):

  model = User
  fields = (
    "bio",
    "email",
    "preference",
    "language",
    "fav_book_cat",
    "fav_movie_cat",
  )
  success_message = "Successfully updated your profile."
  def get_object(self, queryset=None):
    return self.request.user

  template_name = "users/update_profile.html"

  success_url = reverse_lazy("users:profile")

class UpdatePasswordView(LoginOnlyView, SuccessMessageMixin, auth_views.PasswordChangeView):
  template_name = "users/edit_password.html"
  success_url = reverse_lazy("users:update")
  success_message = "Password changed successfully"


def switch_language(request):
    lang = request.GET.get("lang", None)

    if lang is not None:
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        translation.activate(lang)

        response = HttpResponse(status=200)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)

        return response

    return HttpResponse(status=400)