from django.urls import path, include

from rest_framework import routers

from api.views import UserViewSet, GithubViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
  # path('user/github/', GithubViewSet.as_view())
]

urlpatterns += router.urls