from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.utils.translation import gettext_lazy

from movies.models import Movie
from books.models import Book
from .models import FavList

# Create your views here.
@login_required
def toggle_fav(request, pk):
    is_movie = request.GET.get("type") == "movie" and True or False
    next_url = request.GET.get("next")
    obj = None

    user = request.user
    fav_list = None

    try:
        if is_movie:
            obj = Movie.objects.get(pk=pk)
        else:
            obj = Book.objects.get(pk=pk)

        try:
            fav_list = FavList.objects.get(created_by=user)
        except FavList.DoesNotExist:
            fav_list = FavList.objects.create(created_by=user)
            fav_list.save()

        if fav_list is not None:
            if is_movie:
                if obj in fav_list.movies.all():
                    fav_list.movies.remove(obj)
                    messages.add_message(
                        request,
                        messages.INFO,
                        gettext_lazy(f"The movie was removed from favorite list"),
                    )
                else:
                    fav_list.movies.add(obj)
                    messages.add_message(
                        request,
                        messages.INFO,
                        gettext_lazy(f"The movie was added to favorite list"),
                    )
            else:
                if obj in fav_list.books.all():
                    fav_list.books.remove(obj)
                    messages.add_message(
                        request,
                        messages.INFO,
                        gettext_lazy(f"The book was removed from favorite list"),
                    )
                else:
                    messages.add_message(
                        request,
                        messages.INFO,
                        gettext_lazy(f"The book was added to favorite list"),
                    )
                    fav_list.books.add(obj)

        if next_url is not None:
            return redirect(next_url)
        else:
            return redirect(reverse("core:home"))

    except (Movie.DoesNotExist, Book.DoesNotExist):
        return Http404("???")
