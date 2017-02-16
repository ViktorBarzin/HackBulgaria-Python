from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from course_management_system.courses.models import Course
from course_management_system.lectures.models import Lecture
from course_management_system.baseapp.models import Lecturer

from django.http import Http404
from django.http import HttpResponseForbidden
from course_management_system.logged_in.decorators import login_required, is_super_user
from course_management_system.courses.forms import EditCourseForm, CreateCourseForm
# Create your views here.


@login_required('/login')
def course_index(request):
    courses = Course.objects.all().order_by('start_date')
    return render(request, 'course_index.html', locals())


@login_required('/login')
# @is_super_user
def create_course(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        name = form.data.get('name')
        description = form.data.get('description')
        start_date = form.data.get('start_date')
        end_date = form.data.get('end_date')
        form_lecturer = form.data.get('lecturer', None)
        if form_lecturer:
            lecturer = Lecturer.objects.filter(id=form_lecturer).first()
        else:
            lecturer = None
        if form.is_valid():
            form.save()
            status_message = 'Succesffully added a new course!'
        else:
            status_message = 'Something in the input was wrong!'
        # Course.objects.create(name=name, description=description, start_date=start_date, end_date=end_date)
    form = CreateCourseForm()
    return render(request, 'new_course.html', locals())


@login_required('/login')
def course_info(request, course_name):
    course = Course.objects.filter(name__iexact=course_name).first()
    lectures = Lecture.objects.filter(course=course).all()
    if not course:
        raise Http404
    return render(request, 'course_info.html', locals())


@login_required('/login')
# @is_super_user
def edit_course(request, course_name):
    courses = Course.objects.all()
    course = Course.objects.all().filter(name__iexact=course_name).first()

    if not course:
        raise Http404('No such course!')

    if request.method == 'POST':
        form = EditCourseForm(request.POST)
        name = form.data.get('name')
        description = form.data.get('description')
        start_date = form.data.get('start_date')
        end_date = form.data.get('end_date')

        course.description = description
        course.name = name
        import ipdb; ipdb.set_trace()# BREAKPOINT)
        form_lecturer = form.data.get('lecturer', None)
        if form_lecturer:
            course.lecturer = Lecturer.objects.filter(id=form.data['lecturer']).first()

        # Checking if any date was picked
        if start_date:
            course.start_date = start_date
        if end_date:
            course.end_date = end_date
        # course.save()
        if form.is_valid():
            form.save()
            status_message = f'You have successfully updated the {course.name} course!'
        else:
            status_message = 'You have entered some wrong information!'

    form = EditCourseForm(initial=course.__dict__)
    return render(request, 'edit_course.html', locals())

