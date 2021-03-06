from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    
    def new(self):
        from django.db import connection
        cursor.execute("""                                                     
            SELECT * from 'qa_question'
            ORDER BY 'added_at' DESC LIMIT 10""")
        return cursor.fetchall() 
        #return Question.objects.order_by('-added_at')[:10]
    
    def popular(self):
        return super(QuestionManager, self).get_queryset().order_by('rating')


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING, related_name='author_of_question')
    likes = models.ManyToManyField(User, null=True, related_name='who_did_like')
    objects = QuestionManager()
    class Meta:
        db_table = 'question'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'answer'
