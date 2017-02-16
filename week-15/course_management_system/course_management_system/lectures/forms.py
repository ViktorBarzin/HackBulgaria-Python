from django import forms
from course_management_system.lectures.models import Lecture


class CreateLectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'


class EditLectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'
