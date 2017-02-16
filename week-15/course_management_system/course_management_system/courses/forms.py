from django import forms
from course_management_system.baseapp.models import User, Lecturer
from course_management_system.courses.models import Course


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User.objects.filter(email=request.POST.get('email'))
        return user


class EditCourseForm(forms.ModelForm):
    # TODO: set initial value to the lecturer select input
    # lecturer = forms.ModelChoiceField(Lecturer.objects.all())

    class Meta:
        model = Course
        # exclude = ('lecturer',)
        fields = '__all__'
        widgets = {'start_date': forms.SelectDateWidget(years=range(2008, 2040)),
                'end_date': forms.SelectDateWidget(years=range(2008, 2040))}

    # course_name = forms.CharField()
    # description = forms.CharField()
    # start_date = forms.DateField()
    # end_date = forms.DateField()


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {'start_date': forms.SelectDateWidget(years=range(2008, 2040)),
                'end_date': forms.SelectDateWidget(years=range(2008, 2040))}


