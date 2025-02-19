from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, verbose_name="전체 이름")
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="전화번호"
    )
    address = models.TextField(blank=True, null=True, verbose_name="주소")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="생년월일")

    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    class Meta:
        db_table = "user"
        verbose_name = "User"
