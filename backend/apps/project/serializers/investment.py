from rest_framework import serializers

from project.models import Investment, Project
from users.models import User


class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investment
        fields = ['amount', 'status', 'project', 'investor']