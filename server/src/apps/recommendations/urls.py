from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RatingViewSet

rating_list = RatingViewSet.as_view({'get': 'list', 'post': 'create'})

rating_detail = RatingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

app_name = 'recommendation'
urlpatterns = format_suffix_patterns([
    path('', rating_list, name='rating-list'),
    path('<int:pk>/', rating_detail, name='rating-detail'),
])
