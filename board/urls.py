from django.urls import path
from .import views

app_name='board'  #네임 스페이스(소속) - url 경로 이름


urlpatterns=[
    # 질문 목록  - 127.0.0.1:8000/board/
    path('', views.index, name='index'),
    # 상세 페이지 -  127.0.0.1:8000/board/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # 질문 등록 - 127.0.0.1:8000/board/question/create/
    path('question/create/', views.question_create, name='question_create'),
]