from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Student
from .filters import studentFilter

def student_list(request):
    students = Student.objects.all().order_by('name')
    
    myFilter = studentFilter(request.GET, queryset=students)
    students=myFilter.qs
    
    paginator = Paginator(students, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'student/student_list.html', {'page_obj': page_obj,'myFilter':myFilter})
