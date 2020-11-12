from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextField()
    posted_date = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


class WorkExperience(models.Model):
    title = models.CharField(max_length=250)
    workplace = models.CharField(max_length=200)
    discription = models.TextField()
    starting_date = models.DateField()
    ending_date = models.DateField()


class Certificate(models.Model):
    title = models.CharField(max_length=250)
    discription = models.TextField()
    issue_date = models.DateField()
    url = models.URLField()


class Project(models.Model):
    title = models.CharField(max_length=250)
    discription = models.TextField()
    starting_date = models.DateField()
    ending_date = models.DateField()
    url = models.URLField(blank=True)