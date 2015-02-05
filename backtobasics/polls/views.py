from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
# Create your views here.
from django.template import RequestContext, loader

from .models import Question

def index(request):
	#return HttpResponse("Hello, world. Your at the polls index.")
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ",".join([p.question_text for p in latest_question_list])
	#return HttpResponse(output)
	#template = loader.get_template('polls/index.html')
	#context = RequestContext(request, {'latest_question_list': latest_question_list})
	#return HttpResponse(template.render(context))
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html',context)
def detail(request, question_id):

	# try:
	# 	question = Question.objects.get(pk = question_id)

	# except Question.DoesNotExist:
	# 	raise Http404("Question DoesNotExist Exist")
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html',{'question':question})	
	#return HttpResponse("You're  looking at question %s."%question_id)

def results(request, question_id):
	response = "You're loking at the results of question %s."
	return HttpResponse(response %question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s."%question_id)		