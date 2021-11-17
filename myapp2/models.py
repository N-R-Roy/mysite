

from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    hobby = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class EmpInfo(models.Model):
    emp_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)

    def __str__(self):
        return self.emp_id

