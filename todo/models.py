#todo_models.py

from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100) #Todo 제목
    description = models.TextField(blank=True) #Todo에 대한 설명
    # created = models.DateField(default=False) #Todo 생성 일자 (날짜가 자동으로 추가되도록 설정)
    complete = models.BooleanField(default=False) #Todo 완료 여부
    important = models.BooleanField(default=False) #Todo 중요 여부

    #def __str__(self):
        #return self.title
