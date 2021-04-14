from rest_framework import serializers

from core.models import WaitList


class WaitListSerializer(serializers.ModelSerializer):
    """Serializer for wait list objects"""

    class Meta:
        model = WaitList
        fields = ('id', 'name', 'email')
        read_only_fields = ('id',)
