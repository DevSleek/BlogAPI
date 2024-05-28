from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from blog.serializers import PostSerializer
from django.db.models import Count
from django.utils import timezone
from blog.models import Post

now = timezone.now()
week_ago = now - timezone.timedelta(days=7)
month_ago = now - timezone.timedelta(days=30)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )


class NewestPostsListAPIView(ListAPIView):
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')[:7]
    serializer_class = PostSerializer


class MostViewedPostsListAPIView(ListAPIView):
    queryset = Post.objects.filter(is_published=True).order_by('-view_count')[:7]
    serializer_class = PostSerializer


class WeeklyPopularPostsListAPIView(ListAPIView):
    queryset = Post.objects.filter(is_published=True, created_at__gte=week_ago).order_by('-view_count')[:7]
    serializer_class = PostSerializer


class MonthlyPopularPostsListAPIView(ListAPIView):
    queryset = Post.objects.filter(is_published=True, created_at__gte=month_ago).order_by('-view_count')[:7]
    serializer_class = PostSerializer


