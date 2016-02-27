from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # Variables
    question_text=  models.CharField(max_length=200)
    pub_date=   models.DateTimeField("date published")
    
    ### Methods ###
    
    # Prints out the contents of the question
    def __str__(self):
        return self.question_text
    
    # Finds if the question has been posted recently
    def was_published_recently(self):
        return (self.pub_date>= timezone.now()-datetime.timedelta(days=1))
# End of Question class

class Choice(models.Model):
    # Variables
    question=   models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=    models.CharField(max_length=200)
    votes=  models.IntegerField(default=0)
    
    ### Methods ###
    
    # Prints out the contents of the choice
    def __str__(self):
        return self.choice_text
# End of Choice class

# End of File