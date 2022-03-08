from django.urls import path
from . import views

app_name ='poll'  # 네임 스페이스 (소속)

urlpatterns = [
    path('', views.index, name='index'),                # 127.0.0.1:8000/poll/
    # path('cart/', views.cart),                            # 127.0.0.1:8000/cart/
    path('<int:pk>/', views.detail, name='detail'),      #127.0.0.1:8000/poll/1
    path('<int:pk>/vote/', views.vote, name='vote')  #127.0.0.1:8000/poll/1/vote

]