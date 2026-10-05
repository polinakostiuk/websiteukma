from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.specialty_list, name='specialty_list'),
    path('programs/<int:pk>/', views.specialty_detail, name='specialty_detail'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
]


