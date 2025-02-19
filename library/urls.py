"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from catalog.views import (
    BookListAPIView,
    BookDetailAPIView,
    BookCreateAPIView,
    BookSearchAPIView,
    AuthorListAPIView,
)
from users.views import SignInView, SignUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("catalog/book/", BookListAPIView.as_view(), name="book-list"),
    path("catalog/book/<int:id>/", BookDetailAPIView.as_view(), name="book-detail"),
    path("catalog/book/create/", BookCreateAPIView.as_view(), name="book-create"),
    path("catalog/book/search/", BookSearchAPIView.as_view(), name="book-search"),
    path("catalog/author/", AuthorListAPIView.as_view(), name="author-list"),
]
