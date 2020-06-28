from django.db import models

# Create your models here.
class Bug(models.Model):
    """
    A single bug post
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    finished_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return self.name
