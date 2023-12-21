from django.contrib import admin

from courses.models import Course
from users.models import User

admin.site.register(User)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',)

