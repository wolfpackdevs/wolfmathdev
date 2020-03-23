from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  technology = models.CharField(max_length=20)
  image = models.ImageField(default='wolf-logo_D5.png', upload_to='project_pics')
  project_url = models.URLField(default="#")
  github_url = models.URLField(default="#")
  

  def __str__(self):
    return self.title