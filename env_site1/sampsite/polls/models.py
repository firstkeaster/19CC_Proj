from django.db import models

## polls example from django site
## each model is a class, that will include
## fields in database.

import datetime
from django.utils import timezone

## setup column names and datatypes to allow DB create tables.

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        ## when the class was called, like Question.objects.all(),
        ## display question on screen.
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - \
               datetime.timedelta(days=1)

class Choice(models.Model):

    question = models.ForeignKey(Question, \
                                 on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

