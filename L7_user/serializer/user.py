from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=225, required=False)
    email = serializers.CharField(max_length=225, required=False)
    password = serializers.CharField(max_length=225, required=False)
    confirmation = serializers.CharField(max_length=225, required=False)

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def c_u(cls,val):
        if val.get('password') != val.get('confirmation'):
            raise serializers.ValidationError({'message': "Password don't match, please check again"})
        del val['confirmation']
        create = User(**val)
        create.set_password(val.get('password'))
        create.save()
        return create

    def create(self, validated_data):
        if self.context['types'] == 'create':
            return self.c_u(validated_data)
        pass

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"