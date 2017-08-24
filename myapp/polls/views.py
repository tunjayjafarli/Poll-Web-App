# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.

# display the latest 5 questions
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)

