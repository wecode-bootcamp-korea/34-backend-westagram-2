from django.db import models

from users.models import User

class Posting(models.Model):
    user_name   = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postings")
    created_at  = models.DateTimeField(auto_now_add=True)
    image_url   = models.CharField(max_length=200)

    class Meta:
        db_table = "postings"