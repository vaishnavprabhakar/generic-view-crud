from rest_framework import serializers
from .models import User, Poll


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()


    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data.get('username')
        )
        user.save()
        
    
    def update(self, instance , validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.save()


class PollSerializer(serializers.Serializer):

    user = serializers.CharField()
    name = serializers.CharField()
    desc = serializers.CharField()
    created_at = serializers.DateTimeField()


    def create(self, validated_data):

        poll = Poll.objects.create(
            user = validated_data.get('user'),
            name = validated_data.get('name'),
            desc = validated_data.get('desc'),
            created_at = validated_data.get('created_at')
        )
        
    
    def update(self, instance, validated_data):

        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance