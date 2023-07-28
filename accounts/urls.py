from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Default
    path('', include('django.contrib.auth.urls')),
    # Register
    path('register/', views.register, name = 'register'),
]