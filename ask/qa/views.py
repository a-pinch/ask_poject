from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_Get
from django.core.paginator import Paginator
from qa.models import Question
from qa.forms import AskForm

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

@require_GET
def question(request, id):
    try:
	question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404	 
    form = AskForm()
    return render(request, 'question.html', {
        'quest': question, 'form': form
    })

def ask(request)
    if request.method == "POST"
	form = AskForm(request.POST)
	if form.is_valid():
	    ask = form.save()
	    url = ask.get_url()
	    return HttpResponseRedirect(url)
    else:
	form = AskForm()
    return render(request,'add_question.html', {
	'form': from
    })
