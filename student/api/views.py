from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student  
from .serializers import StudentSerializer  

class GetStudents(APIView):
    def get(self, request):
        class_filter = request.GET.get('class')
        data_selection = request.GET.get('data')

        # Retrieve all students
        students = Student.objects.all()

        # Apply class filter if class_filter parameter is provided
        if class_filter:
            students = students.filter(class_level=class_filter)

        # Sort the students based on the total_score property using Python's sorted function
        sorted_students = sorted(students, key=lambda x: x.total_score(), reverse=True)

        if sorted_students:
            serializer = StudentSerializer(sorted_students, many=True, context={'request': request})
            data = serializer.data

            # Check if data_selection parameter is provided to customize serializer fields
            if data_selection:
                fields = data_selection.split(',')
                data = [self.filter_fields(student, fields) for student in data]

            return Response(data)
        else:
            return Response({"message": "No students found"}, status=404)

    def filter_fields(self, student_data, fields):
        return {key: student_data[key] for key in fields if key in student_data}