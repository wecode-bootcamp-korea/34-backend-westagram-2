from django.db import models

# Create your models here.
class User(models.Model):
    username     = models.CharField(max_length=45)
    first_name   = models.CharField(max_length=45)
    last_name    = models.CharField(max_length=45)
    email        = models.EmailField(max_length=300, unique=True)
    password     = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'


