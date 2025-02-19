# Create your views here.
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny

from catalog.serializer import BookSerializer
from users.permissions import IsAdminGroup, IsStaffGroup, IsAdminOrStaffGroup
from .models import Book


# 책 목록 조회 ListAPIView
class BookListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# 특정 책 조회 RetriveAPIView
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminOrStaffGroup()]


# 책 등록 CreateAPIView
# 책 수정
# 책 삭제
# 책 검색

# 저자 목록 조회
# 저자 상세 조회
# 저자 등록
# 저자 수정
# 저자 삭제

# 카테고리 목록 죄회
# 카테고리 추가
