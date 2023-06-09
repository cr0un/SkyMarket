from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту


class UserRoles:
    # TODO закончите enum-класс для пользователя
    USER = 'user'
    ADMIN = 'admin'

    CHOICES = (
        (USER, _('User')),
        (ADMIN, _('Admin')),
    )


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, role=UserRoles.USER, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None, role='admin'):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role,
            password=password,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user




