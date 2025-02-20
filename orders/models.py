from django.db import models

# Create your models here.
from users.models import User
from catalog.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_order")

    STATUS_CHOICES = [
        ("pending", "Pending"),  # 주문 접수
        ("paid", "Paid"),  # 결제 완료
        ("shipped", "Shipped"),  # 배송 중
        ("delivered", "Delivered"),  # 배송 완료
        ("canceled", "Canceled"),  # 주문 취소
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending"
    )  # 주문 상태
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}님의 {self.book.title} 책의 주문 상태는 {self.status} 입니다."
