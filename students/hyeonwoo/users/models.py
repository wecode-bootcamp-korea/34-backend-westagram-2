from decimal import MAX_EMAX
from django.db import models

class User(models.Model):
    name               = models.CharField(max_length=45)
    email              = models.CharField(max_length=45)
    password           = models.CharField(max_length=45)
    mobilephone_number = models.CharField(max_length=45)

    class Meta:
        db_table = "users"