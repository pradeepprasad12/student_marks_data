from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'class_level', 'total_score')
    search_fields = ('name', 'roll_number')
    list_filter = ('class_level',)
