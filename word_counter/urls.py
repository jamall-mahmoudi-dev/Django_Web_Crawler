from django.urls import path
from . import views

app_name = 'word_counter'

urlpatterns = [
    path('', views.index, name='home'),
]