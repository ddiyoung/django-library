from django.db.models import QuerySet

from ..models import Book

from typing import List


class BookServices:
    @staticmethod
    def search_book(
        title: str = None,
        author: List[str] = None,
        category: List[str] = None,
        publisher: str = None,
    ) -> QuerySet[Book]:
        query = Book.objects.all()

        if title:
            query = query.filter(title__contains=title)

        if author:
            query = query.filter(author__in=author)

        if category:
            query = query.filter(categories__in=category)

        if publisher:
            query = query.filter(publisher__in=publisher)

        return query
