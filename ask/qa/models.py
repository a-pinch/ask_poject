from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField(blank = True)
	author = User()
	likes = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	author = User()
