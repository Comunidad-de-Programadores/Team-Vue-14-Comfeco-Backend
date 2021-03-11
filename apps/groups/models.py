from django.db import models
from apps.core.models import CoreTimeModel

# Create your models here.
class Group(CoreTimeModel):
    name = models.CharField("Name", max_length=250)
    description = models.TextField()
    tag = models.CharField("Tag", max_length=50)
    image = models.ImageField("image", upload_to="image/")

    class Meta:
        """Meta definition for Group."""

        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        """Unicode representation of Group."""
        return self.name
