from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Customer(models.Model):
    customer_id = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_date = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_point = models.CharField(max_length=200)
    def __str__(self):
        return self.customer_text
    