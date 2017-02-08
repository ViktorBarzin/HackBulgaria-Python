from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
# Create your views here.

from course_management_system.courses.models import Course
from course_management_system.lectures.models import Lecture


def create_lecture(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('lecture_name')
        week = int(request.POST.get('week'))
        course = Course.objects.filter(id=request.POST.get('course_id_selector')).first()
        url = request.POST.get('lecture_url')

        Lecture.objects.create(name=name, week=week, course=course, url=url)
        # create_lecture is for visualizing in html
        created_lecture = 'You have successfully added a new lecture!'

        # TODO: refreshing the page generates new post request so consider
        # redirecting to somewhere?

    return render(request, 'create_lecture.html', locals())


def show_lecture(request, lecture_id):
    lecture = Lecture.objects.filter(id=lecture_id).first()
    if not lecture:
        raise Http404('No such lecture!')
    return render(request, 'lecture_info.html', locals())


def edit_lecture(request, lecture_id):
    lecture = Lecture.objects.filter(id=lecture_id).first()
    courses = Course.objects.all()
    if not lecture:
        raise Http404('There is no lecture with this id!')
    if request.method == 'POST':
        name = request.POST.get('lecture_name')
        week = int(request.POST.get('lecture_week'))
        course = Course.objects.filter(id=request.POST.get('course_id_selector')).first()
        url = request.POST.get('lecture_url')

        # Totally ignoring error checking here
        lecture.name = name
        lecture.week = week
        lecture.course = course
        lecture.url = url
        lecture.save()
        # return render(request, 'lecture_info.html', locals())
        # return show_lecture(request, lecture.id)
        # return redirect('https://www.google.com')
        return redirect(f'/lecture/{lecture.id}')

    return render(request, 'edit_lecture.html', locals())


