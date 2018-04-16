from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=10, blank=False)
    last_name = models.CharField(_('last name'), max_length=10, blank=False)
    tel = models.CharField(_('tel number'), blank=False,
                           unique=True, max_length=12)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text='admin site へのアクセス権限.'
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'アカウント削除の代わりにこちらをFalseにしてください.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tel']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
