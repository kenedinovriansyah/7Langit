from .base import Base
from django.db import models
from django.utils import timezone
from nanoid import generate
from .context import Status

class TBSchedulers(models.Model):
    public_id = models.CharField(max_length=225, unique=True, null=False, default=generate())
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class TBCategory(models.Model):
    public_id = models.CharField(max_length=225, unique=True, null=False, default=generate())
    name = models.CharField(max_length=225, null=False)
    status = models.SmallIntegerField(choices=Status.choice, default=Status.active)

class TBEvent(Base):
    public_id = models.CharField(max_length=225, unique=True, null=False, default=generate())
    name = models.CharField(max_length=225, null=False)
    banner = models.ImageField(upload_to="banner/", null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=225, null=False)
    address = models.CharField(max_length=225, null=False)
    country = models.CharField(max_length=225, null=False)
    province = models.CharField(max_length=225, null=False)
    district = models.CharField(max_length=225, null=False)
    region = models.CharField(max_length=225, null=False)
    organization_name = models.CharField(max_length=225, null=False)
    category = models.ForeignKey(TBCategory, on_delete=models.CASCADE)
    schedulers = models.ForeignKey(TBSchedulers, on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)