import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_misgrations = True

    def _valid_cpf(self, cpf):
        if len(cpf) != 14:
            raise ValueError(_('The cpf field is not valid'))

    def valid_fields(self, email, first_name, last_name,
                    cpf, password, avatar=None):
        if not email:
            raise ValueError(_('The email field is required'))

        if not first_name:
            raise ValueError(_('The first_name field is required'))

        if not last_name:
            raise ValueError(_('The last_name field is required'))

        if not cpf:
            raise ValueError(_('The cpf field is required'))

        self._valid_cpf(cpf)

        if not password:
            raise ValueError(_('The password field is required'))
        if len(password) < 6:
            raise ValueError(_(
                'The password field must be at least 6 characters'
            ))

    def create_user(self, email, first_name, last_name,
                    cpf, password, avatar=None):
        self.valid_fields(
            email, first_name, last_name, cpf, password, avatar=None
        )
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, cpf=cpf,
            avatar=avatar
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name,
                    cpf, password, avatar=None):
        self.valid_fields(
            email, first_name, last_name, cpf, password, avatar=None
        )
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, cpf=cpf,
            avatar=avatar
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user
