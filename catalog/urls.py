from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookCreateAPIView,
    BookSearchAPIView,
    AuthorListAPIView,
)

urlpatterns = [
    path("book/", BookListAPIView.as_view(), name="book-list"),
    path("book/<int:id>/", BookDetailAPIView.as_view(), name="book-detail"),
    path("book/create/", BookCreateAPIView.as_view(), name="book-create"),
    path("book/search/", BookSearchAPIView.as_view(), name="book-search"),
    path("author/", AuthorListAPIView.as_view(), name="author-list"),
]
