from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.crypto import get_random_string
from users.managers import UserManager
from users.managers import UserRoles


# class UserRoles:
#     # TODO закончите enum-класс для пользователя
#     USER = 'user'
#     ADMIN = 'admin'
#
#     CHOICES = (
#         (USER, _('User')),
#         (ADMIN, _('Admin')),
#     )


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=UserRoles.CHOICES)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def is_superuser(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_staff(self):
        return self.role == UserRoles.ADMIN

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    objects = UserManager()



