from django.db import models

# Create your models here.
class CoreTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'CoreTimeModel'
        verbose_name_plural = 'CoreTimeModels'
        abstract = True