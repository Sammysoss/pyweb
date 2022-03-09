from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from poll.models import Question

@login_required(login_url='common:login')
def index(request):
    question_list = Question.objects.all()
    return render(request, 'poll/index.html', {'question_list': question_list})

def detail(request, pk):
    question = Question.objects.get(id=pk)
    return render(request, 'poll/detail.html', {'question': question})


def vote(request, pk):
    question = Question.objects.get(id=pk)
    if request.method == "POST":
        try:
            choice = request.POST['choice']
        except:
            error = '항목을 선택하세요.'
            return render(request, 'poll/detail.html',
                          {'question':question, 'error':error})
        else:
            sel_choice = question.choice_set.get(id=choice)
            sel_choice.votes += 1
            sel_choice.save()
            return render(request, 'poll/result.html', {'question':question})
    else:
        return render(request, 'poll/detail.html', id=pk)

