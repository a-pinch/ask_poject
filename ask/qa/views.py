from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from qa.models import Question
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def main(request):
    questions = Question.objects.order_by('-added_at')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'fresh_questions.html', {
	'quests': page.object_list,
        'paginator': paginator, 'page': page,
    })

def popular(request):
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular?page='
    page = paginator.page(page)
    return render(request, 'fresh_questions.html', {
	'quests': page.object_list,
        'paginator': paginator, 'page': page,
    })

def question(request, id):
    try:
	question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404	 
    form = AskForm()
    return render(request, 'question.html', {
        'quest': question, 'form': form
    })

@csrf_exempt
def ask(request):
    if request.method == "POST":
	form = AskForm(request.POST)
	if form.is_valid():
            ask = form.save()
	    url = ask.get_url()
	    return HttpResponseRedirect(url)
    else:
	form = AskForm()
    return render(request,'add_question.html', {
	'form': form
    })

@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
	question = form.save()
	url = question.get_url()
	return HttpResponseRedirect(url)
    question = Question.objects.get(pk=form.question)
    return render(request, 'question.html', {
	'quest': question, 'form': form
    })

@csrf_exempt
def user_signup(request):
    if request.method == 'POST':
	form = SignupForm(request.POST)
	if form.is_valid():
	    user = form.do_signup()
	    if user is not None:
                login(request, user)
 	        return HttpResponseRedirect('/')
    else:
	form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
	form = LoginForm(request.POST)
	if form.is_valid():
	    user = form.do_login()
	    if user:
	        login(request, user)
	        return HttpResponseRedirect('/')
    else:
	form = LoginForm()
    return render(request, 'login.html', {'form':form})
