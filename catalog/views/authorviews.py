from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from catalog.serializer import AuthorSerializer
from users.permissions import IsAdminOrStaffGroup
from ..models import Author


# 저자 목록 조회
class AuthorListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


# 저자 조회
# 저자 수정
# 저자 삭제
class AuthorDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminOrStaffGroup()]


# 저자 등록
class AuthorCreateAPIView(CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAdminOrStaffGroup]


# 저자 검색
class AuthorSearchAPIView(GenericAPIView):
    serializer_class = AuthorSerializer
    permission_classes = []
    queryset = Author.objects.all()

    def post(self, request):
        name = request.data.get("name")
        author = Author.objects.filter(name__contains=name)
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)
