from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField("Name", max_length=250)
    image = models.ImageField(upload_to="banner/")
    description = models.TextField()
    event_date = models.DateTimeField()

    class Meta:
        """Meta definition for Event."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Event."""
        return self.name
