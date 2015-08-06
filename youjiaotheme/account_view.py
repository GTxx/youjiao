# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.views.generic.base import View, TemplateView
from django.contrib.auth import authenticate, login, logout


class LoginView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/activities/1')
            elif user.is_staff:
                return redirect('/activities/1')
            elif user.is_active:
                return redirect('/activities/1')
        return redirect('/activities/1')


class LogoutView(View):
    def get(self, request):
        logout(request)
