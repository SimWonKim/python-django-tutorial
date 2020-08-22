import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

'''
    모델을 작성하므로써 django가 알아서 
    DB의 테이블 생성 및 모델 접근에 필요한 API를 만들어 준다.
    
    models.CharField : 글자수가 제한된 텍스트를 정의 할때 사용.
    models.TextField : 글자수가 제한이 없는 긴 텍스트를 정의할때 사용.
    models.DateTimeField : 날짜와 시간을 의미.
    models.ForeignKey : 다른 모델과 관계(링크)를 의미.
'''


class Question(models.Model):
    # model 이름은 Question.
    # models는 Question이 django의 모델임을 의미.

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    # machine friendly 한 형식의 field name
    pub_date = models.DateTimeField('date published')
    # human friendly 한 형식의 field name


class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # django는 1대 1, 1대 다, 다대 다 관계를 지원함.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


