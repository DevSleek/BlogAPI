from django.urls import path
from blog.views import NewestPostsListAPIView, MostViewedPostsListAPIView, \
    WeeklyPopularPostsListAPIView, MonthlyPopularPostsListAPIView

urlpatterns = [
    path('', NewestPostsListAPIView.as_view()),
    path('most_viewed/', MostViewedPostsListAPIView.as_view()),
    path('weekly/', WeeklyPopularPostsListAPIView.as_view()),
    path('monthly/', MonthlyPopularPostsListAPIView.as_view())
]