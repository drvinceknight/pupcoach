from django.db import models

class Behaviour(models.Model):
    """A model for a behaviour"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    acquired = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')

    class Meta:
        ordering = ('acquired',)

    def __str__(self):
        return self.title
