from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserViewSet

user_detail = UserViewSet.as_view({'post': 'create'})

# custom_user_detail = CustomUserViewSet.as_view({'post': 'create'})

app_name = 'user'
urlpatterns = format_suffix_patterns([
    path('', user_detail, name='user-detail'),
    # path('/old', custom_user_detail, name='custom-user-detail'),
])
