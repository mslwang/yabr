from rest_framework import viewsets

from .models import Rating
from .serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for ratings.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer