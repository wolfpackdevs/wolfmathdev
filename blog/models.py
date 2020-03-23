from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Inital models: https://www.djangorocks.com/tutorials/how-to-create-a-basic-blog-in-django/defining-your-models.html
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    # slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # image = models.ImageField(default="{% static '/img/wolf-logo_D5.png' %}", upload_to='blog_pics')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        