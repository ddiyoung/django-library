from django.urls import path

from .views import OrderDetailAPIView, OrderListAPIView, OrderCreateAPIView

urlpatterns = [
    path("order/", OrderListAPIView.as_view(), name="order-list"),
    path("order/<int:id>", OrderDetailAPIView.as_view(), name="order-detail"),
    path("order/create/", OrderCreateAPIView.as_view(), name="order-create"),
]
