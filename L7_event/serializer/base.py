from rest_framework import serializers
from django.contrib.auth.models import User
from database.models.event import TBCategory, TBSchedulers

class BaseScheduler(serializers.Serializer):
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField()

    class Meta:
        abstract = True

class BaseCategory(serializers.Serializer):
    name_category = serializers.CharField(max_length=225,required=False)
    status = serializers.IntegerField(default=0)

    class Meta:
        abstract = True

class BaseEvent(serializers.Serializer):
    name = serializers.CharField(max_length=225,required=False)
    banner = serializers.ImageField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    location = serializers.CharField(max_length=225, required=False)
    address = serializers.CharField(max_length=225, required=False)
    country = serializers.CharField(max_length=225, required=False)
    province = serializers.CharField(max_length=225, required=False)
    district = serializers.CharField(max_length=225, required=False)
    region = serializers.CharField(max_length=225, required=False)
    organization_name = serializers.CharField(max_length=225, required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=TBCategory.objects.all(),required=False)
    schedulers = serializers.PrimaryKeyRelatedField(queryset=TBSchedulers.objects.all(),required=False)

    class Meta:
        abstract = True
