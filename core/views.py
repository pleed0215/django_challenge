import os
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

from movies.models import Movie
from books.models import Book
from people.models import Person
from categories.models import Category
from django.conf import settings

def resolve_home(request):
  page = int(request.GET.get("page", 1))
  page_size = 10
  all_people = Person.objects.all().order_by("-created_at")[:page_size*3]
  all_books = Book.objects.all().order_by("-year")[:page_size*3]
  all_movies = Movie.objects.all().order_by("-year")[:page_size*3]

  all_objects = []
  for i in range(30):
    all_objects.append({
      "person": all_people[i],
      "book": all_books[i],
      "movie": all_movies[i],
    })

  paginator = Paginator(all_objects, page_size)
  try:
      page = paginator.page(page)

      return render(request, "home.html", context={"page": page, "page_title": "Home", },)
  except EmptyPage:
      return redirect("/")


def resolve_search(request):
  search_term = request.GET.get ("search-term", None)

  found_movies = Movie.objects.filter(title__icontains=search_term)
  found_books = Book.objects.filter(title__icontains=search_term)
  found_people = Person.objects.filter(Q(name__icontains=search_term)|Q(kind__icontains=search_term))
  found_genres = Category.objects.filter(Q(name__icontains=search_term)|Q(kind__icontains=search_term))
  
  print(found_books)
  return render(request, "search.html", context={"page_title": "Search", "search_by": search_term, "movies": found_movies, "books": found_books, "people": found_people, "categories": found_genres})