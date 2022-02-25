from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from new.models import Cquestion ,Cchoise
# Create your views here.
# Create your views here.
def index(request):
  latest_question_list = Cquestion.objects.all().order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'new/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Cquestion, pk=question_id)
    return render(request, 'new/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Cquestion, pk=question_id)
    try:
        selected_choice = question.cchoise_set.get(pk=request.POST['choice'])
    except (KeyError, Cchoise.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'new/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('new:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Cquestion, pk=question_id)
    return render(request, 'new/results.html', {'question': question})