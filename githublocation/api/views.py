from api.serializers import UserSerializer, UserGithubSerializer

from rest_framework import viewsets
from users.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import renderers
from rest_framework import status

from django.http import HttpResponse, JsonResponse
from django.conf import settings

import requests, json, locale


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


# # class GithubViewSet(APIView): only post
# class GithubViewSet(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
#   # serializer_class = UserSerializer
#   serializer_class = UserGithubSerializer

#   # queryset = User.objects.all()

#   # print("queryset ========", type(queryset))
#   # queryset = ""

#   def get_queryset(self):
#     username = self.kwargs.get('username')
#     queryset = requests.get("https://api.github.com/users/" + username)
#     print("queryset =======", queryset.content)

#     # queryset = super(GithubViewSet, self).get_queryset()
#     # return queryset.filter(id=1)
#     return queryset


class GithubViewSet(APIView):
  def get(self, request, username):

    headers = {'Authorization': 'access_token '+ settings.ACCESS_TOKEN +''}
    queryset = requests.get("https://api.github.com/users/" + username, headers=headers).json()

    response = renderers.JSONRenderer().render(
      queryset, 'application/json'
    )

    return HttpResponse(response, content_type='application/json')


class ZipCodeViewSet(APIView):
  def get(self, request, zipcode):
    queryset = requests.get("https://viacep.com.br/ws/"+ zipcode +"/json/").json()

    response = renderers.JSONRenderer().render(
      queryset, 'application/json'
    )

    return HttpResponse(response, content_type='application/json')
