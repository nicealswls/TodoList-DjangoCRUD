from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    # mytodo_urls.py에 todo.urls를 연결시킴
    # todo/로 시작되는 모든 url들은 todo 폴더 안 urls.py에서 관리한다는 뜻
    path('todo/', include('todo.urls')),
]
