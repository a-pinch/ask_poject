from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def new():
		pass
	def popular():
		pass

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField(blank = True)
	author = models.ForeignKey(User)
	test22 = models.CharField(max_length = 10)
	likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	author = models.ForeignKey(User)
