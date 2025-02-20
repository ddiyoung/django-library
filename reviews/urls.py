from django.urls import path

from .views import (
    ReviewLitAPIView,
    ReviewCreateAPIView,
    ReviewDetailAPIView,
    LikeCreateAPIView,
    LikeUpdateAPIView,
)

urlpatterns = [
    path(
        "review/<int:book>/<int:id>/",
        ReviewDetailAPIView.as_view(),
        name="review-detail",
    ),
    path("review/<int:book>/", ReviewLitAPIView.as_view(), name="review-list"),
    path("review/create/", ReviewCreateAPIView.as_view(), name="review-create"),
    path("like/create/", LikeCreateAPIView.as_view(), name="like-create"),
    path("like/update/<int:id>/", LikeUpdateAPIView.as_view(), name="like-update"),
]
