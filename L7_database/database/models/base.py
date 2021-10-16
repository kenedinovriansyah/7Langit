from django.contrib.auth.models import User
from django.db import models


class BaseSoft(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class BaseForeignKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class BaseTimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True

class Base(BaseSoft,BaseForeignKey,BaseTimeStamps):
    class Meta:
        abstract = True