from rest_framework import serializers

from ..users.serializers import UserSerializer
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()

    class Meta:
        model = Rating
        fields = '__all__'
        depth = 1
