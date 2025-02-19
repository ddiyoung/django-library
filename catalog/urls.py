from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookCreateAPIView,
    BookSearchAPIView,
    AuthorListAPIView,
    AuthorDetailAPIView,
    AuthorCreateAPIView,
    AuthorSearchAPIView,
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryDetailAPIView,
    CategorySearchAPIView,
)

urlpatterns = [
    path("book/", BookListAPIView.as_view(), name="book-list"),
    path("book/<int:id>/", BookDetailAPIView.as_view(), name="book-detail"),
    path("book/create/", BookCreateAPIView.as_view(), name="book-create"),
    path("book/search/", BookSearchAPIView.as_view(), name="book-search"),
    path("author/", AuthorListAPIView.as_view(), name="author-list"),
    path("author/<int:id>/", AuthorDetailAPIView.as_view(), name="author_detail"),
    path("author/create/", AuthorCreateAPIView.as_view(), name="author-create"),
    path("author/search/", AuthorSearchAPIView.as_view(), name="author-search"),
    path("category/", CategoryListAPIView.as_view(), name="category-list"),
    path("category/<int:id>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("category/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path("category/search/", CategorySearchAPIView.as_view(), name="category-search"),
]
