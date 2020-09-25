from django import template
from books.models import Book
from movies.models import Movie

register = template.Library()

@register.simple_tag(takes_context=True)
def is_reviewed(context, obj_pk, is_movie):
    
    obj = None
    
    try:
      if is_movie:
        obj = Movie.objects.get(pk=obj_pk)
      else:
        obj = Book.objects.get(pk=obj_pk)

      if obj is not None:
        review_filtered = obj.reviews.filter(created_by=context.request.user)
        if review_filtered.count()>0:
            return True
        else:
            return False

        return False
    except (Movie.DoesNotExist, Book.DoesNotExist):
        return False
