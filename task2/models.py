from django.db import models

# Create your models here.
class TaskTwo(models.Model):
    SINO = models.IntegerField()
    title = models.CharField(max_length=20, default="")
    parentID = models.Field(blank=True)

    def __str__(self):
        return self.title

