from rest_framework.viewsets import ModelViewSet
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Avg, Count

class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name"]


    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        university = self.get_object()
        courses = university.universitycourse_set.all()
        course_title = request.query_params.get('title')
        semester = request.query_params.get('semester')

        if course_title:
            courses = courses.filter(course__title__icontains=course_title)
        if semester:
            courses = courses.filter(semester__icontains=semester)

        courses = courses.order_by('duration_weeks')
        serializer = UniversityCourseSerializer(courses, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def course_stats(self, request, pk=None):
        university = self.get_object()
        stats = university.universitycourse_set.aggregate(
            total_courses=Count('id'),
            average_duration=Avg('duration_weeks')
        )

        return Response({
            'total_courses': stats['total_courses'],
            'average_duration': round(stats['average_duration'] or 0, 1)
        })


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title"]


class UniversityCourseViewSet(ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['university__name', 'course__title']
    ordering_fields = ["duration_weeks"]
    filterset_fields = {
        "course__title": ["exact", "contains"],
        "semester": ["exact", "contains"],
        "duration_weeks": ["gte", "lte", "exact"]
    }