from rest_framework import serializers

from lessons.models import Lesson


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'email',
            'phone',
            'country'
        )