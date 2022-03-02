from django.urls import path
from .import views

urlpatterns=[
    path('', views.index),                                  # 127.0.0.1:8000/board/
    path('<int:question_id>/', views.detail),     # 127.0.0.1:8000/board/1/

]