from django.urls import path
from rest_framework.authtoken import views
from .views import KarmaListView, KarmaDetailView

urlpatterns = [
    path('tasks', KarmaListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', KarmaDetailView.as_view(), name='tasks'),
]