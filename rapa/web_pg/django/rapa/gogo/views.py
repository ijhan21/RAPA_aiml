from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from gogo.models import Cquestion1 ,Cchoise1
# Create your views here.
# Create your views here.
def index(request):
  latest_question_list = Cquestion1.objects.all().order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'gogo/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Cquestion1, pk=question_id)
    return render(request, 'gogo/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Cquestion1, pk=question_id)
    try:
        selected_choice = question.cchoise1_set.get(pk=request.POST['choice'])
    except (KeyError, Cchoise1.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'gogo/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('gogo:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Cquestion1, pk=question_id)
    return render(request, 'gogo/results.html', {'question': question})