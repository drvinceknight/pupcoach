from django.db import models

class Behaviour(models.Model):
    """A model for a behaviour"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    acquired = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('acquired',)
