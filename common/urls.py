from django.urls import path
from django.contrib.auth import views


app_name = 'common'

urlpatterns = [
    # LoginView 클래스 - 제네릭 뷰
    path('login/', views.LoginView.as_view(), nama='login' ),

]