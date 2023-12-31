from rest_framework import serializers
from student.models import Student  

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'subject1','subject1_score', 'subject2','subject2_score', 'subject3','subject3_score', 'subject4','subject4_score', 'subject5', 'subject5_score','image', 'class_level', 'total_score']
