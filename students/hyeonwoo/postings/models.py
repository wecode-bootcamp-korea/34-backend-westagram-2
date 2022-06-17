from django.db import models

from users.models import User

class Posting(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postings")
    created_at   = models.DateTimeField(auto_now_add=True)
    image_url    = models.URLField()
    postname     = models.CharField(default='', max_length=50)
    contents     = models.TextField(default='')

    class Meta:
        db_table = "postings"