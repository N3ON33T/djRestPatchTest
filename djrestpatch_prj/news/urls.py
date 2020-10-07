from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as news_views

urlpatterns = [
    path('news/', news_views.NewsList.as_view()),
    path('news/<int:pk>/', news_views.NewsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)