from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),    # mytodo_urls.py에 todo.urls를 연결시킴
]
