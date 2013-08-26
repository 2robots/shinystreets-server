from django.forms import widgets
from rest_framework import serializers
from shinystreetsapp.models import Area


class AreaSerializer(serializers.Serializer):
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=False,
                                  max_length=100)
    nodes = serializers.CharField(widget=widgets.Textarea,
                                 max_length=100000)
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