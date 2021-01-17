import pandas as pd
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from ..ratings.models import Ratings
from .models import Batch, Recommendation
from .serializers import BatchSerializer, RecommendationSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for ratings.
    """
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


# class ComputeRecommendationsView(generics.GenericAPIView):
#     queryset = Ratings.objects.all()
#     serializer_class = RecommendationSerializer

#     def get(self, request, pk, *args, **kwargs):
#         df = pd.DataFrame.from_records(self.get_queryset().values('user_id', 'book_id', 'rating'))
