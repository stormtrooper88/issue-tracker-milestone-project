from django.db import models
from decimal import Decimal
import datetime

# Create your models here.
class Features(models.Model):
    """
    A single feature post
    """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    finished_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('50.00'))


    def __str__(self):
        return self.name
