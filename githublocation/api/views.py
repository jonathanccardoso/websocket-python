from api.serializers import UserSerializer

from rest_framework import viewsets
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer

  # def get_permissions(self):
  #   """
  #   Instantiates and returns the list of permissions
  #   that this view requires.abs
  #   """
  #   permission_classes = [IsAuthenticated]
  #   return [permission() for permission in permission_classes]
