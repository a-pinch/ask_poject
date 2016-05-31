from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length = 255)
    text = forms.CharField(widget = forms.Textarea)
    def __init__(self, user, *args, **kwargs):
	super(AskForm, self).__init__(*args, **kwargs)
    def clean_title(self):
	title = self.cleaned_data['title']
	if not title:
	    raise forms.ValidationError("Title cann't be empty ")
    def clean_text(self):
	text =self.cleaned_data['text']
	if not text:
	    raise form.ValidationError("Please enter text")
    def save(self):
	ask = Question(**self.cleaned_data)
	ask.save()
	return ask

class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.CharField(widget = forms.HeddenInput())
    def __init__(self, user, *args, **kwargs):
	super(AnswerForm, self).__init__(*args, **kwargs)
    def clean_text(self):
	text =self.cleaned_data['text']
	if not text:
	    raise form.ValidationError("Please enter text")
    def save(self):
	answer = Answer(**self.cleaned_data)
	return answer
