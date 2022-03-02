from django.http import HttpResponse
from django.shortcuts import render
from board.models import Question, Answer


def index(request):
    question_list = Question.objects.all()         # db에서 전체 검색
    return render(request, 'board/question_list.html', {'question_list':question_list})
    # return HttpResponse('<h2>Hello~ Django!!</h2>')

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'board/detail.html', {'question':question})