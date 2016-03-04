from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
	# Variables
	template_name=	"polls/index.html"
	context_object_name=	"latest_question_list"
	
	# --- Methods ---
	
	# Returns the last five published questions
	def get_queryset(self):
		return Question.objects.order_by("-pub_date")[:5]
	####
# End of IndexView

class DetailView(generic.DetailView):
	# Variables
	template_name=	"polls/detail.html"
	model=	Question
# End of DetailView

class ResultsView(generic.DetailView):
	# Variables
	template_name=	"polls/results.html"
	model=	Question
# End of ResultView

def vote(request, question_id):
	question=	get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=	question.choice_set.get(pk=request.POST["choice"])
	except (KeyError, Choice.DoesNotExist):
		return render(request, "polls/detail.html", {
			"question":	question,
			"error_message":	"You didn't select a choice"
		})
	else:
		selected_choice.votes+=	1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# End of File