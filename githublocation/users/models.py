from django.db import models


class User(models.Model):
  name = models.CharField('Nome', max_length=80, null=False, blank=False)
  username = models.CharField('Username Github', max_length=50, null=False, blank=False)
  zipcode = models.CharField('CEP', max_length=50, null=False, blank=False)
