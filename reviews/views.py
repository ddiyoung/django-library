from django.shortcuts import render
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from .models import Review
from reviews.serializer.reviewserializer import ReviewSerializer
from users.permissions import IsCustomerGroup

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
    permission_classes = [IsCustomerGroup]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewCreateAPIView(CreateAPIView):
    permission_classes = [IsCustomerGroup]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
