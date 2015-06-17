import datetime

from django.db import models
from django.utils import timezone


class visitor_tracking(models.Model):
    ip = models.CharField(max_length=30, primary_key=True)
    recent = models.DateTimeField()

    def update(self):
        if self.recent <= timezone.now()-datetime.timedelta(minutes=30):
            self.recent = timezone.now()
            self.save()

    def __str__(self):
        return self.ip
