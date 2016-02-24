from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from try_forms_app.forms import AuthForm


class AuthView(FormView):
    form_class = AuthForm
    template_name = 'try_forms_app/auth.html'
