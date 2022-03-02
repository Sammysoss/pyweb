from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from board.forms import QuestionForm
from board.models import Question, Answer


def index(request):
    # 질문 목록
    # question_list = Question.objects.all()                                      # db에서 전체 검색
    question_list = Question.objects.order_by('-create_date')         # '-' 내림차순, '-pk'도 가능
    return render(request, 'board/question_list.html', {'question_list':question_list})
    # return HttpResponse('<h2>Hello~ Django!!</h2>')

def detail(request, question_id):
    # 상세 페이지
    question = Question.objects.get(id=question_id)
    return render(request, 'board/detail.html', {'question':question})

def question_create(request):
    # 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # 내용이 작성된 폼
        if form.is_valid():  # 폼이 있다면,
            question = form.save(commit=False)  # 임시 저장 (날짜x)
            question.create_date = timezone.now()
            question.save()  # 실제 저장(날짜 O)
            return redirect('board:index')  # 질문 목록 페이지 이동
    else: # request.method == 'GET':
        form = QuestionForm()  # 질문 등록 폼 - 객체 변수 생성 (비어있는 폼)
    return render(request, 'board/question_form.html', {'form':form})  # 공통


