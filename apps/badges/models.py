from django.db import models

# Create your models here.
class Badge(models.Model):

    class Meta:

        verbose_name = 'Badge'
        verbose_name_plural = 'Badges'

    def __str__(self):
        """Unicode representation of Badge."""
        pass
