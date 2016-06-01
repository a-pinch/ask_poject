from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length = 255)
    text = forms.CharField(widget = forms.Textarea)
#    def __init__(self, *args, **kwargs):
#	super(AskForm, self).__init__(*args, **kwargs)
    def clean_title(self):
	title = self.cleaned_data['title']
	if not title:
            raise forms.ValidationError("Title cann't be empty ")
	return title
    def clean_text(self):
	text =self.cleaned_data['text']
	if not text:
	    raise form.ValidationError("Please enter text")
	return text
    def save(self):
	self.cleaned_data['author_id'] = 1
	return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.IntegerField(widget = forms.HiddenInput())
    def __init__(self, *args, **kwargs):
	super(AnswerForm, self).__init__(*args, **kwargs)
    def clean_text(self):
	text =self.cleaned_data['text']
	if not text:
	    raise form.ValidationError("Please enter text")
    def save(self):
	answer = Answer(**self.cleaned_data)
	answer.save()
	return answer.question

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    def do_signup(self):
	return User.objects.create_user(self.cleaned_data.username, 
		self.cleaned_data.email, self.cleaned_data.password)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    def do_login(self):
	return  authenticate(self.cleaned_data.username, self.cleaned_data.password)
