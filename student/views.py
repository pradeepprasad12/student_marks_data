from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Student
from .filters import studentFilter
from .forms import StudentForm
from django.contrib import messages


def student_list(request):
    students = Student.objects.all().order_by('name')
    myFilter = studentFilter(request.GET, queryset=students)
    students=myFilter.qs
    paginator = Paginator(students, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'student data uplode successfully..')
            form = StudentForm()
        else:
            messages.warning(request, 'student data uplode failed..')

    else:
        form = StudentForm()
    return render(request, 'student/student_list.html', {'page_obj': page_obj,'myFilter':myFilter,'form': form})
