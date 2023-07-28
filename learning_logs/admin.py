from django.contrib import admin

from .models import Topic, Entry

admin.site.register(Topic)
'''manage the models via the site'''
admin.site.register(Entry)

