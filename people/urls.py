from django.urls import path
from people.views import PeopleListView, PersonDetailView, PersonCreateView, PersonUpdateView

app_name="people"

urlpatterns = [
  path("", PeopleListView.as_view(), name="people"),
  path("<int:pk>/", PersonDetailView.as_view(), name="detail"),
  path("<int:pk>/update", PersonUpdateView.as_view(), name="update"),
  path("create/", PersonCreateView.as_view(), name="create"),
]
