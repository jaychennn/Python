from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''Learning Topics'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) # auto time recorder
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # When the account is deleted, so does the topic

    def __str__(self):
        '''return the string representation'''
        return self.text
    '''Django model field reference'''

class Entry(models.Model):
    '''the knowledge learned'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # 级联删除
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''return an entry ,50 letters at most '''
        if len(self.text) <= 50:
            return f"{self.text[:50]}"
        else: return f"{self.text[:50]}..."