from django.contrib import admin
from .models import University, Course, UniversityCourse


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(UniversityCourse)
class UniversityCourseAdmin(admin.ModelAdmin):
    list_display = ('display_university', 'display_course', 'semester', 'duration_weeks')
    list_filter = ('university', 'semester')
    search_fields = ('university__name', 'course__title', 'semester')

    def display_university(self, obj):
        return obj.university.name

    display_university.short_description = 'University'

    def display_course(self, obj):
        return obj.course.title

    display_course.short_description = 'Course'