from django.contrib import admin
from .models import MainPage,Department,Specialty, Teacher

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head_name")

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "department", "coordinator_name")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree", "department")