from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from catalog.serializer import BookSerializer
from users.permissions import IsAdminOrStaffGroup
from ..models import Book, Author
from ..services.bookservices import BookServices


# 책 목록 조회 ListAPIView
class BookListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# 특정 책 조회
# 특정 책 수정
# 특정 책 삭제
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminOrStaffGroup()]


# 책 등록 CreateAPIView
class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAdminOrStaffGroup]


# 책 검색
class BookSearchAPIView(GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        title = request.data.get("title")
        author = request.data.getlist("author_ids")
        category = request.data.getlist("category_ids")
        publisher = request.data.get("publisher_ids")

        books = BookServices.search_book(
            title=title, author=author, category=category, publisher=publisher
        )

        serializer = self.get_serializer(books, many=True)

        return Response(serializer.data)
