from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

from django.shortcuts import render
## render a page whenever it passed a template, or any data
## that is required by that template, i.e. list of our questions.

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
## Avoid submitting twice. if the user would click the
## back button, this will avoid sending data multiple
## different times.
from django.urls import reverse
## return a url we can point to, based on whatever
## the current question is we are dealing.

from .utils.test_plot import *

## use template to separate design from code.

# def index(request):
#     return HttpResponse("We're in the polls index!")


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    ## Find the name for the data we'er going to pass
    ## into the template.
    ## each key in context is a variable name
    ## appears in template.
    context = {
        'latest_question_list': latest_question_list,
    }
    ## render: pass the request, url template, and params to be
    ## passed to template.
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        ## Here, 'choice' should refer to 'name' in html input.
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def testPlotter(request, maxSize):
#     ## run the test plot function, parse maxSize to
#     ## the func, and possibly plot the figure.
#     figDir = plotFunc(maxSize)
#     # figDir = figDir.replace('\\', '/')
#     return render(request, 'polls/plots.html', {'figDir': str(figDir),})

def testPlotter(request, maxSize):
    ## run the test plot function, parse maxSize to
    ## the func, and possibly plot the figure.
    figName = plotFunc(maxSize)
    # new_img = IMG(
    #     img=request.FILES.get('img'),
    #     name=request.FILES.get('img').name
    # )
    # new_img.save()
    # figDir = figDir.replace('\\', '/')
    return render(request, 'polls/plots.html', {'figName': str(figName),})

def t34Tank(request):
    return HttpResponse("This is a T34 tank's picture")


