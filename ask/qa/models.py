from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User, null=False, on_delete=models.DO_NOTHING)
    likes = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.OneToOneField(Question, null=False, on_delete=models.DO_NOTHING)
    author = models.OneToOneField(User, null=False, on_delete=models.DO_NOTHING)
    
class User(User)
