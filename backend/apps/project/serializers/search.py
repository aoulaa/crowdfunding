from rest_framework import serializers

from project.models import Project


class ProjectSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id', 'images', 'title', 'details', 'target', 'start_date', 'end_date', 'creation_date', 'creator',
            'category', 'tags', 'videos', 'days_remaining')
        read_only_fields = ('id', 'creator')

