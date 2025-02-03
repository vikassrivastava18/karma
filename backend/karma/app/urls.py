from django.urls import path

from .views import (KarmaListView, KarmaDetailView, 
                    ToDoListView, ToDoDetailView, 
                    ReflectionView, HomeView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks', KarmaListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', KarmaDetailView.as_view(), name='task'),
    path('todos', ToDoListView.as_view(), name='todos'),
    path('todos/<int:pk>', ToDoDetailView.as_view(), name='todo'),
    path('reflections', ReflectionView.as_view(), name='todos'),
]