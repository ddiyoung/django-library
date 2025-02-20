from django.urls import path

from .views import ReviewLitAPIView, ReviewCreateAPIView

urlpatterns = [
    path("review/<int:book>", ReviewLitAPIView.as_view(), name="review-list"),
    path("create/<int:book>", ReviewCreateAPIView.as_view(), name="review-create"),
]
