
from django.db import models


class EmpInfo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)

    def __str__(self):
        return self.name




