from rest_framework import viewsets, mixins

from waitlist import serializers

from core.models import WaitList


class CreateWaitListView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage a new wait listing in the system"""
    queryset = WaitList.objects.all()
    serializer_class = serializers.WaitListSerializer

    def perform_create(self, serializer):
        """Waitlist Addition"""
        serializer.save(waitlist=self.request.data)
