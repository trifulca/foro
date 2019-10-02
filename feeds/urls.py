from django.urls import path
from feeds.feeds import ActiveTopicsFeed

urlpatterns = [
    path('active.xml', ActiveTopicsFeed())
]
