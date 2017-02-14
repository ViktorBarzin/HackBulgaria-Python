from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from course_management_system.courses.models import Course
from course_management_system.lectures.models import Lecture

from django.http import Http404
from django.http import HttpResponseForbidden
from course_management_system.logged_in.decorators import login_required, is_super_user
# Create your views here.


@login_required('/login')
def course_index(request):
    courses = Course.objects.all().order_by('start_date')
    return render(request, 'course_index.html', locals())


@login_required('/login')
# @is_super_user
def create_course(request):
    if request.method == 'POST':
        name = request.POST.get('course_name').rstrip()
        description = request.POST.get('course_description').rstrip()
        start_date = request.POST.get('course_start_date')
        end_date = request.POST.get('course_end_date')

        Course.objects.create(name=name, description=description, start_date=start_date, end_date=end_date)
    return render(request, 'new_course.html', locals())


@login_required('/login')
def course_info(request, course_name):
    course = Course.objects.filter(name__iexact=course_name).first()
    lectures = Lecture.objects.filter(course=course).all()
    if not course:
        raise Http404
    return render(request, 'course_info.html', locals())


@login_required('/login')
@is_super_user
def edit_course(request, course_name):
    courses = Course.objects.all()
    course = Course.objects.all().filter(name__iexact=course_name).first()

    if not course:
        raise Http404('No such course!')

    if request.method == 'POST':
        name = request.POST.get('course_name')
        description = request.POST.get('course_description')
        start_date = request.POST.get('course_start_date')
        end_date = request.POST.get('course_end_date')

        course.description = description
        course.name = name
        # Checking if any date was picked
        if start_date:
            course.start_date = start_date
        if end_date:
            course.end_date = end_date
        course.save()
        successfully_updated_msg = f'You have successfully updated the {course.name} course!'

    return render(request, 'edit_course.html', locals())

