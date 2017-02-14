from django.shortcuts import render, redirect
from django.http import Http404
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from course_management_system.baseapp.models import User
from course_management_system.logged_in.decorators import login_required, redirect_if_logged
from course_management_system.courses import views as course_views
# Create your views here.


@redirect_if_logged(redirect_url='/profile')
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # TODO: hash password
        try:
            User.objects.create(email=email, password=password)
        except IntegrityError:
            user_exists = 'User with that email already exists'
            return render(request, 'register.html', locals())
        # return HttpResponseRedirect('course/')
        return redirect('/course/')

    return render(request, 'register.html', locals())


# Add redirect to profile if logged in
# @check_session_by('email')
@redirect_if_logged('/profile')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            if password == user.password:
                request.session['email'] = email
                request.user = user
                return redirect('/profile')
                return course_views.course_index(request)
        raise Http404('No such user!')
    return render(request, 'login.html', locals())


# @check_session_by('email')
@login_required(redirect_url='/login')
def profile(request):
    user = User.objects.filter(email=request.session.get('email')).first()

    return render(request, 'profile.html', locals())


@login_required(redirect_url='/login')
def logout(request):
    request.session.flush()
    return redirect('/login')
