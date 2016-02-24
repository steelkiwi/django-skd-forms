from django.contrib.auth.forms import AuthenticationForm

from skd_forms.mixins import SKDFormMixin


class AuthForm(SKDFormMixin, AuthenticationForm):
    pass
