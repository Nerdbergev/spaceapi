from django.db import models
from datetime import datetime

# Create your models here.

class DoorStatus(models.Model):
    UNKNOWN = "unknown"
    OPEN = "open"
    CLOSE = "close"

    doorStatus = [
        (UNKNOWN, 'unknown'),
        (OPEN, 'open'),
        (CLOSE, 'close')
    ]
    status = models.CharField(max_length=255, choices=doorStatus)
    date = models.DateTimeField(default=datetime.now)

