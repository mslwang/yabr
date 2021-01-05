from rest_framework import serializers

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'rating', 'user_id', 'book_id', 'time_created']
