
from django.urls import path,include
from student.api.views import GetStudents


urlpatterns = [
    path('GetStudents/',GetStudents.as_view())


]