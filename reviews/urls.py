from django.urls import path
from .views import ReviewCreateView, delete_review

app_name = "reviews"

urlpatterns = [
    path("<int:pk>/", ReviewCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", delete_review, name="delete"),
]