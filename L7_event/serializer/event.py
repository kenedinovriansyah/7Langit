from rest_framework import serializers
from .base import BaseEvent
from database.models.event import TBEvent
from .category import CategoryModelSerializer
from .schedulers import SchedulerModelSerializer
from django.conf import settings

class EventSerializer(BaseEvent):
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def c_e(cls,val):
        create = TBEvent(**val)
        create.save()
        return create

    def create(self, validated_data):
        if self.context['types'] == 'create':
            return self.c_e(validated_data)
        pass

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class EventModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(read_only=True)
    schedulers = SchedulerModelSerializer(read_only=True)
    class Meta:
        model = TBEvent
        exclude = ["id",]

    # banner = serializers.SerializerMethodField('get_banner')

    # def get_banner(self,val):
    #     try:
    #         if val.banner:
    #             return val.banner
    #     except UnicodeDecodeError:
    #         return settings.MEDIA_URL + 'notimage/images.png'