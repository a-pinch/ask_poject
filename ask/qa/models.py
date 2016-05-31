from django.db import models
from django.core.urlresolvers import reverse
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
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name='likes_set')


	def get_url(self):
	    return reverse('quest', args=[self.id])
	def __unicode__(self):
	    return self.title


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	author = models.ForeignKey(User)

	def __unicode__(self):
	    return self.text
