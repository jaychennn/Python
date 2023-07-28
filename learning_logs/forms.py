# 用户添加表单form
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta: # built-in class
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})} #widgets是一种小部件，用于控制文本框、下拉列表等
