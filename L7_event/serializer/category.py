from rest_framework import serializers
from .base import BaseCategory
from database.models import TBCategory


class CategorySerializer(BaseCategory):
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def c_c(cls,val,extra):
        val['name'] = val.get('name_category')
        del val['name_category']
        create = TBCategory(**val)
        create.save()
        extra.context['category'] = create
        return create

    def create(self, validated_data):
        if self.context['types'] == 'create':
            return self.c_c(validated_data,self)
        pass

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBCategory
        exclude = ["id"]