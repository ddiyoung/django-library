from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

# Create your views here.
from .serializer import OrderSerializer
from .models import Order
from users.permissions import (
    IsOwnerUser,
    IsAdminOrStaffGroup,
    IsOwnerUserOrIsAdminOrStaffGroup,
)


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if IsAdminOrStaffGroup().has_permission(self.request, self):
            return Order.objects.all()

        return Order.objects.filter(user=user)


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsOwnerUserOrIsAdminOrStaffGroup()]  # 권한을 OR 조건으로 결합
        return [IsAdminOrStaffGroup()]


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
