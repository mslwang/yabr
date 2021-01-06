from django.urls import path

from .views import RatingViewSet

rating_list = RatingViewSet.as_view({'get': 'list', 'post': 'create'})

rating_detail = RatingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

app_name = 'rating'
urlpatterns = [
    path('rating/', rating_list, name='rating-list'),
    path('rating/<int:pk>/', rating_detail, name='rating-detail'),
]
