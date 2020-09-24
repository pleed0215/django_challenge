# Coding Challenge

## Admin login: id - admin, pw - admin

- [x] Make a new URL /favs/add/<int:pk> and a function based view.
  - This URL should add a movie or a book to the user's favourite list, for example /favs/add/1?type=book or /favs/add/2?type=movie

- [x] The user should be logged in to perform this action.
- [x] If the user has no fav list the view should create one.
- [x] On the movie and book template mixin make a button to add them to the user's fav list.
- [x] Make a template tag to show if a book or movie is already on the fav list.