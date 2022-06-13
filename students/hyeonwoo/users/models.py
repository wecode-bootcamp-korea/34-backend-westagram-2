from decimal import MAX_EMAX
from django.db import models

class User(models.Model):
    first_name    = models.CharField(max_length=45, blank=False)
    last_name     = models.CharField(max_length=45, blank=False)
    user_name     = models.CharField(max_length=45, unique=True, blank=False)
    email         = models.EmailField(max_length=45, unique=True, blank=False)
    password      = models.CharField(max_length=45 , blank=False)
    mobile_number = models.CharField(max_length=45, blank=False)

    class Meta:
        db_table = "users"