from django.db import models
class SourceRecord(models.Model):
    source = models.CharField(max_length=100)
    external_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    payload = models.JSONField(default=dict)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("source","external_id")