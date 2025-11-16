from django.db import models
from django.contrib.auth.models import User
from apps.quiz.models import Quiz


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    guest_username = models.CharField(max_length=15, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.user:
            return (f'{self.user.username} : {self.content[:20]}')
        return (f'{self.guest_username} : {self.content[:20]}')  

