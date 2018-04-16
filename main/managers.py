from django.contrib.auth.base_user import BaseUserManager
from django.db.models import QuerySet


class UserQuerySet(QuerySet):
    def only_user(self):
        pass


class UserManager(BaseUserManager):
    """ユーザーマネージャー."""

    use_in_migrations = True

    def _create_user(self, email, tel, password, **extra_fields):
        """Create and save a user with the given username, email, and
        password."""
        if not email:
            raise ValueError('Email Address を設定してください')
        email = self.normalize_email(email)
        if not tel:
            raise ValueError("電話番号を設定してください")
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, tel=tel, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, tel, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, tel, password, **extra_fields)

    def create_superuser(self, email, tel, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, tel, password, **extra_fields)

    def get_query_set(self):
        return UserQuerySet(self.model)

    def __getattr__(self, attr, *args):
        # 詳しくは https://code.djangoproject.com/ticket/15062 を参照
        if attr.startswith("_"):
            raise AttributeError
        return getattr(self.get_query_set(), attr, *args)
