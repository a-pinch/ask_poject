from django.test import TestCase
from ask.qa import Question
from django.contrib.auth import User 

ngo.contrib.auth.model 
def testQuestion(self):
#	question = Question.object.create()
	user,_ = User.object = get_or_create(username='x', password = 'y')
	question = Question(title = 'qwe', text = 'qwe', author = user)
	question.save()
	assertIsNotNone(question.id, 'question id is None')

