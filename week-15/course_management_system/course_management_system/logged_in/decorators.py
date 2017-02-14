from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps
from django.http import HttpResponseRedirect
from course_management_system.baseapp.models import User


def login_required(redirect_url):
    def accepter(func):
        @wraps(func)
        def check_session(request, *args, **kwargs):
            if request.session.get('email', False):
                return func(request, *args, **kwargs)
            return redirect(redirect_url)
        return check_session
    return accepter


def redirect_if_logged(redirect_url):
    def redirect(func):
        # @wraps
        def accepter(request, *args, **kwargs):
            if User.objects.filter(email=request.session.get('email', False)).first():
                # return redirect(redirect_url)
                print(request.session.get('email'))
                return HttpResponseRedirect(redirect_url)

            return func(request, *args, **kwargs)
        return accepter
    return redirect


def is_super_user(func):
    @wraps(func)
    def accepter(request, *args, **kwargs):
        user = User.objects.filter(email=request.session.get('email', None)).first()
        if user and user.is_lecturer:
            return func(request, *args, **kwargs)
        raise PermissionDenied
    return accepter
