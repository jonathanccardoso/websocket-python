from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from api import views as api_views


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user/github/<str:username>', api_views.GithubViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
