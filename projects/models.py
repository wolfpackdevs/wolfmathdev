from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  technology = models.CharField(max_length=20)
  image = models.FilePathField(path='/img/')
  project_url = models.URLField(default="#")
  github_url = models.URLField(default="#")
  created_on = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title