from django.db import models

class SessionInfo(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=100)
    last_seen = models.DateTimeField(auto_now=True)
