from django.db import models

class User(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    email         = models.EmailField(max_length=45, unique=True)
    password      = models.CharField(max_length=45)
    phone_number  = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'users'