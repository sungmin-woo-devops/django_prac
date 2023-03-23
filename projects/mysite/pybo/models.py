from django.db import models

# Create your models here.
# SQL문에서 create에 해당하는 부분
class Question(models.Model):
    subject = models.CharField(max_length=200) # 글자수 제한이 있는 문자열
    content = models.TextField()               # 글자수 제한이 없는 문자열
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content