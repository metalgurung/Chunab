from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #we want to Link Foreignkey to PK as to relate choices with Question class 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #ondelete=mdels cascade -> when the question is deleted the choice models field aslso be deleted likewise
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text