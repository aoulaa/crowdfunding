from rest_framework import serializers

from project.models import Project, Category


class ProjectFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'images', 'title', 'details', 'target', 'start_date', 'end_date', 'creation_date', 'creator',
            'category', 'tags', 'videos', 'days_remaining')
        read_only_fields = ('id', 'creator')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
