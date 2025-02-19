# 카테고리 목록 죄회
# 카테고리 추가
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from catalog.serializer import CategorySerializer
from users.permissions import IsAdminOrStaffGroup
from ..models import Category


# 카테고리 목록 조회
class CategoryListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# 저자 조회
# 저자 수정
# 저자 삭제
class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminOrStaffGroup()]


# 저자 등록
class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrStaffGroup]


# 저자 검색
class CategorySearchAPIView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = []
    queryset = Category.objects.all()

    def post(self, request):
        name = request.data.get("name")
        author = Category.objects.filter(name__contains=name)
        serializer = CategorySerializer(author, many=True)
        return Response(serializer.data)
