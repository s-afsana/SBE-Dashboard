from rest_framework import serializers, viewsets
from .models import SourceRecord
class SourceRecordSerializer(serializers.ModelSerializer):
    class Meta: model=SourceRecord; fields="__all__"
class SourceRecordViewSet(viewsets.ModelViewSet):
    queryset = SourceRecord.objects.all().order_by("-updated_at")
    serializer_class = SourceRecordSerializer
