from rest_framework import viewsets

from courses.models import Course
from courses.serilzers import CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
