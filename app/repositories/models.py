import uuid

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.validators import ASCIIUsernameValidator


class AccountModel(models.Model):
    account_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class UserModel(models.Model):
    username_validator = ASCIIUsernameValidator()
    account =  models.ForeignKey('AccountModel', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)

