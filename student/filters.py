import django_filters
from .models import Student

class studentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['name','roll_number','class_level']