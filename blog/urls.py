from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.all_courses, name='all_courses'),
    path('<int:blog_id>/', views.detail, name='detail')

  
]