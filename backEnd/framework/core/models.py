
from typing import Reversible
from django.db import models

# Create your models here.
class Wall(models.Model):
    origin=models.URLField()
    destination=models.URLField()
    description=models.TextField()
    class Meta:
        managed = True
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return Reversible("Wall_detail", kwargs={"pk": self.pk})