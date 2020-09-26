from django.urls import path
from .views import LoginView, logout_view, SignupView, UserDetailView, UpdateProfileView, UpdatePasswordView, switch_language

app_name = "users"

urlpatterns = [
  path("login/", LoginView.as_view(), name="login"),
  path("logout/", logout_view, name="logout"),
  path("signin/", SignupView.as_view(), name="create"),
  path("me/", UserDetailView.as_view(), name="profile"),
  path("me/update/", UpdateProfileView.as_view(), name="update"),
  path("me/password/", UpdatePasswordView.as_view(), name="password"),
  path("switch_lang/", switch_language, name="switch_lang"),
]