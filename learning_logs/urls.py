'''Define the learning_logs URL mode'''

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 空字符串与基础url匹配
    path('', views.index, name = 'index'),
    # Django将查找基础url后紧跟topics的URL
    path('topics/', views.topics, name = 'topics'),
    # 在上面的基础上添加topic_id实参
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # 添加新主题
    path('new_topic/', views.new_topic, name = 'new_topic'),
    # 添加新条目
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    # 编辑条目
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
]
