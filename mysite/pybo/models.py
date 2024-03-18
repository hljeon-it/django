from django.db import models


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)   # 글자 수가 제한된 텍스트
    content = models.TextField()   # 글자 수가 제한되지 않는 텍스트
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   # ForeignKey는 다른 속성과 연결할 때, CASCADE는 Question이 삭제되면 Answer도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()