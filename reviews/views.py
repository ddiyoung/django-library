from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny

from .models import Review, Like
from reviews.serializer.reviewserializer import ReviewSerializer
from users.permissions import IsCustomerGroup, IsOwnerUser
from .serializer.likeserializer import LikeSerializer


# Create your views here.


class ReviewLitAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs.get("book")

        if book_id:
            return Review.objects.filter(book=book_id)

        return Review.objects.all()


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsOwnerUser()]


class ReviewCreateAPIView(CreateAPIView):
    permission_classes = [IsCustomerGroup]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeCreateAPIView(CreateAPIView):
    permission_classes = [IsCustomerGroup]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeUpdateAPIView(UpdateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "id"
