from django.urls import path

from .views import RatingViewSet

ratings_list = RatingViewSet.as_view({'get': 'list', 'post': 'create'})

ratings_detail = RatingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

app_name = 'ratings'
urlpatterns = [
    path('ratings/', ratings_list, name='ratings-list'),
    path('ratings/<int:pk>/', ratings_detail, name='ratings-detail'),
]
