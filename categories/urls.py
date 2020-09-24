from django.urls import path
from categories.views import CategoryDetailView, CategoryListView

app_name="categories"

urlpatterns = [
  path("", CategoryListView.as_view(), name="categories"),
  path("<int:pk>/", CategoryDetailView.as_view(), name="detail"),
]
