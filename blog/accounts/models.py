from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, related_query_name='user')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        related_query_name='user'
    )