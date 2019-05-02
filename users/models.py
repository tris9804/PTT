from django.db import models
from django.contrib.auth.models import  AbstractUser

class User(AbstractUser):
    email = models.EmailField('電子郵件', unique=True)
    name = models.CharField('id名稱', unique=True, max_length=20)
    nickname = models.CharField('暱稱', max_length=10)

