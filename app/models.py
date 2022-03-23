from distutils.command.upload import upload
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Topics(models.Model):
    topic = models.CharField(max_length=30)
    topic_image = models.ImageField(upload_to='topic_icon/')

    def __str__(self):
        return self.topic

class Whats(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    what = models.TextField(max_length=200)

    def __str__(self):
        return str(self.what)

class Whens(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    when = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.when)

class Whys(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    why = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.why)

class Hows(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    how = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.how)

class Typses(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    types = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.types)

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    feedback = models.TextField(max_length=2000)