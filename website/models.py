from django.db import models
import datetime

# Create your models here.

class AppUser(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  image_url = models.CharField(max_length=100)
  email = models.CharField(max_length=200)
  password = models.CharField(max_length=100)
  location = models.CharField(max_length=200)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class BlogPost(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  date_posted = models.DateField(default=datetime.date.today)
  number_of_comments = models.PositiveIntegerField(default=0)
  image_url = models.CharField(max_length=500)

  def __str__(self):
    return f"{self.title}"


class Comment(models.Model):
  user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
  blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(default=datetime.datetime.now)
  content = models.TextField()


class Service(models.Model):
  name = models.CharField(max_length=255)
  summary_image_url = models.CharField(max_length=500)
  detail_image_url = models.CharField(max_length=500)
  description = models.TextField()

  def __str__(self):
    return f"{self.name}"


class ServiceDetail(models.Model):
  name = models.CharField(max_length=255)
  stage = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=7, decimal_places=2)

  def __str__(self):
    return f"{self.name}"
