from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('course-detail/<int:id>/', course_dt_view, name='course-dt'),
    path('blog/', blog_view, name='blog'),
    path('tasks/', give_task, name='tasks')
]