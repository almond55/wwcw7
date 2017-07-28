from django.http import Http404
from django.conf import settings
from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.decorators import login_required

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password', 'password1', 'password2'))

class TopPage(View):
    def get(self, request, *args, **kwargs):
        _TEMPLATE_PATH = "top.html"
        response_dict = {}
        return render(request, _TEMPLATE_PATH, response_dict)

class WWCSignupView(SignupView):
    @sensitive_post_parameters_m
    def dispatch(self, request, *args, **kwargs):
        return super(SignupView, self).dispatch(request, *args, **kwargs)

class ProfilePage(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        _TEMPLATE_PATH = "profile.html"
        response_dict = {}
        return render(request, _TEMPLATE_PATH, response_dict)
    
