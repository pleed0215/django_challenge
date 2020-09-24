from django.urls import path
from .views import MoviesListView, MovieDetailView, MovieCreateView, MovieUpdateView

app_name="movies"

urlpatterns = [
  path("", MoviesListView.as_view(), name="movies"),
  path("<int:pk>/", MovieDetailView.as_view(), name="detail"),
  path("<int:pk>/update", MovieUpdateView.as_view(), name="update"),
  path("create/", MovieCreateView.as_view(), name="create"),
]
