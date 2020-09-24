from django.urls import path

from .views import toggle_fav

app_name="favs"

urlpatterns = [
  path("add/<int:pk>", toggle_fav, name="toggle"),
]