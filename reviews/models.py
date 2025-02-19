from django.db import models

from users.models import User
from catalog.models import Book


# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Book과 1:N 관계
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User와 1:N 관계
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "book"], name="unique_review"),
        ]

    def __str__(self):
        return f"{self.user.username} 님의 {self.book.title} 리뷰"


class Like(models.Model):
    STATUS_CHOICES = [
        ("like", "Like"),
        ("hate", "Hate"),
        ("none", "None"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="none",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저
    review = models.ForeignKey(Review, on_delete=models.CASCADE)  # 리뷰

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "review"], name="unique_like"),
        ]

    def __str__(self):
        return f"{self.user.username} 님이 {self.review.book.title}의 리뷰({self.review.title})를 {self.status} 합니다."
