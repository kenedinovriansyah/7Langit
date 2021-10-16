from rest_framework import serializers
from .base import BaseScheduler
from database.models import TBSchedulers


class SchedulerSerializer(BaseScheduler):
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def c_s(cls,val,extra):
        create = TBSchedulers(**val)
        create.save()
        extra.context['schedulers'] = create
        return create

    def create(self, validated_data):
        if self.context['types'] == 'create':
            return self.c_s(validated_data,self)
        pass

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class SchedulerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBSchedulers
        exclude = ["id"]