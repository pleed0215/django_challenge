from django import template
from books.models import Book
from movies.models import Movie
from favs.models import FavList

register = template.Library()


@register.simple_tag(takes_context=True)
def is_in_fav(context, obj_pk, is_movie):
    
    obj = None
    
    try:
      if is_movie:
        obj = Movie.objects.get(pk=obj_pk)
      else:
        obj = Book.objects.get(pk=obj_pk)

      if obj is not None:
        try:
          fav_list = FavList.objects.get(created_by=context.request.user)
          
          if is_movie:
            if obj in fav_list.movies.all():
              return True
            else:
              return False
          else:
            if obj in fav_list.books.all():
              return True
            else:
              return False

        except FavList.DoesNotExist:
          return False

      return False
    except (Movie.DoesNotExist, Book.DoesNotExist):
      return False
