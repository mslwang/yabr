from rest_framework import serializers

from .models import Batch, Recommendation


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'
        depth = 1