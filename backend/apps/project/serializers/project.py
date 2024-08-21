from rest_framework import serializers
from project.models import Project, ProjectImage, ProjectVideo, Tag, Category

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('path',)

class ProjectVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectVideo
        fields = ('path',)

class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = ProjectImageSerializer(many=True, required=False)
    videos = ProjectVideoSerializer(many=True, required=False)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        videos_data = validated_data.pop('videos', [])
        tags_data = validated_data.pop('tags', [])
        project = Project.objects.create(**validated_data)
        for image_data in images_data:
            ProjectImage.objects.create(project=project, **image_data)
        for video_data in videos_data:
            ProjectVideo.objects.create(project=project, **video_data)
        project.tags.set(tags_data)
        return project

    class Meta:
        model = Project
        fields = (
            'id', 'images', 'title', 'details', 'target', 'start_date', 'end_date', 'creation_date', 'creator', 'category', 'tags', 'videos')
        read_only_fields = ('id', 'creator')