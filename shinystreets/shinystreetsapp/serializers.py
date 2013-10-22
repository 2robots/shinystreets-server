from django.forms import widgets
from rest_framework import serializers
from shinystreetsapp.models import Area


class AreaSerializer(serializers.Serializer):
    id = serializers.Field()
    name = serializers.CharField(required=False, max_length=100)
    nodes = serializers.CharField(widget=widgets.Textarea, max_length=100000)
    active = serializers.BooleanField(required=False)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.nodes = attrs.get('nodes', instance.nodes)
            instance.active = attrs.get('active', instance.active)
            return instance

        # Create new instance
        return Area(**attrs)

class IssueSerializer(serializers.Serializer):
    id = serializers.Field()
    title = serializers.CharField(required=False, max_length=100)
    location = serializers.CharField(required=False, max_length=100)
    description = serializers.CharField(widget=widgets.Textarea, max_length=100000)
    solved = serializers.BooleanField(required=False)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.name = attrs.get('title', instance.title)
            instance.nodes = attrs.get('location', instance.location)
            instance.description = attrs.get('description', instance.description)
            instance.solved = attrs.get('solved', instance.solved)
            return instance

        # Create new instance
        return Issue(**attrs)

class UserSerializer(serializers.Serializer):
    id = serializers.Field()
    email = serializers.CharField(required=False, max_length=100)
    bio = serializers.CharField(widget=widgets.Textarea, max_length=100000)
    avatar = serializers.CharField(required=False, max_length=100)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.email = attrs.get('email', instance.email)
            instance.bio = attrs.get('bio', instance.bio)
            avatar.description = attrs.get('avatar', instance.avatar)
            return instance

        # Create new instance
        return Issue(**attrs)