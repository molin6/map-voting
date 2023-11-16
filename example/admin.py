from django.contrib import admin

from django.db import models

class StateSelection(models.Model):
    state_id = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.state_name} ({self.state_id})"
