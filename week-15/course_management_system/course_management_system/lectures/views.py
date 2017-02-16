from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
# Create your views here.

from course_management_system.courses.models import Course
from course_management_system.lectures.models import Lecture
from course_management_system.lectures.forms import CreateLectureForm, EditLectureForm


def create_lecture(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CreateLectureForm(request.POST)
        name = form.data.get('name')
        import ipdb; ipdb.set_trace()# BREAKPOINT)

        # if Lecture.objects.filter(name=name)
        week = int(form.data.get('week'))
        course = Course.objects.filter(id=form.data.get('course')).first()
        url = form.data.get('url')

        Lecture.objects.create(name=name, week=week, course=course, url=url)
        if form.is_valid():
            form.save()
            status_message = 'You have successfully added a new lecture!'
        else:
            status_message = 'You have entered invalid data!'

        # TODO: refreshing the page generates new post request so consider
        # redirecting to somewhere?
    form = CreateLectureForm()
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

    form = EditLectureForm(initial=lecture.__dict__)
    return render(request, 'edit_lecture.html', locals())


