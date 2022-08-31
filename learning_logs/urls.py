"""Defines URL pattern for learning logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page showing all topics
    path('topics/', views.topics, name='topics'),
    # Page for one topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editting an existing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for removing entry and redirect to topic page
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # Page for removing topic and redirect to topics page
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]