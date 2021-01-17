from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserViewSet

user_detail = UserViewSet.as_view({'post': 'create'})
user_detail_get = UserViewSet.as_view({'get': 'retrieve'})

# custom_user_detail = CustomUserViewSet.as_view({'post': 'create'})

app_name = 'users'
urlpatterns = format_suffix_patterns([
    path('users/', user_detail, name='user-detail'),
    path('users/<int:pk>/', user_detail_get, name='user-detail-2'),
    # path('/old', custom_user_detail, name='custom-user-detail'),
])
