from django.db import models
from . import managers

class User(models.Model):
    
    object = managers.UserManager()

