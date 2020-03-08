from django.db import models

# Create your models here.
class MathNotebook(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    notebook_url = models.URLField(default="#")

    class Meta:
        ordering = ['-created_on']