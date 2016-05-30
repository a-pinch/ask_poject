from django.test import TestCase
from django.contrib.auth.models import User 

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE']  = "ask.settings"


class TestQuestion(TestCase):
    def testQuestion(self):
	from qa.models import Question
#	question = Question.object.create()
#       assert False, "Test"
        user,_ = User.objects.get_or_create(username='x', password = 'y')
	try:
            question = Question(title = 'qwe', text = 'qwe', author = user)
            question.save()
	except:
	    assert False, "Failed to create question model"
        assertIsNone(question.id, 'question id is None')

