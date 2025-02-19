from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from catalog.serializer import BookSerializer, AuthorSerializer
from users.permissions import IsAdminOrStaffGroup
from ..models import Book, Author


# 저자 목록 조회
class AuthorListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


# 저자 조회
# 저자 수정
# 저자 삭제
# class AuthorDetailAPIView()
# 저자 등록
