import os
from . import managers
from django.db import models
from banco_web import settings
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.signals import post_delete


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    cpf = models.CharField(_('cpf'), max_length=14)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(
        _('avatar'), upload_to='avatars/', null=True, blank=True
    )

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cpf']

    class Meta:
        ordering = (
            'cpf', 'email', 'first_name', 'last_name',
        )


@receiver(post_delete, sender=User)
def delete_user_avatar(sender, instance, **kwargs):
    if instance.avatar:
        avatar_file = os.path.join(settings.MEDIA_ROOT, str(instance.avatar))
        try:
            os.remove(avatar_file)
        except FileNotFoundError:
            print(_(f'File not found: {instance.avatar.path}'))
