from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('post/', views.todo_post, name='todo_post'), # 생성 url은 post/로 지정
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'), # 수정 url은 /edit/로 지정
    path('done/', views.done_list, name='done_list'),
    path('done/<int:pk>/', views.todo_done, name='todo_done'),
]