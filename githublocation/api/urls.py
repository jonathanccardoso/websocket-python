from django.urls import path, include

from rest_framework import routers

from easydiet.api.views import UserViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
]

urlpatterns += router.urls