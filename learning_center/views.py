from django.shortcuts import render
from .models import *


def home_view(request):
    teachers = TeacherModel.objects.all()
    courses = LevelModel.objects.all()
    return render(request, 'home.html', {'teachers': teachers,
                                         'courses': courses})
#


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def blog_view(request):
    works = LevelModel.objects.all()
    return render(request, 'blog.html', {'works': works})


def course_dt_view(request, id):
    courses = LevelModel.objects.filter(id=id).all()

    return render(request, 'course-detail.html', {'courses': courses})


def give_task(request):
    return render(request, 'give_task.html')