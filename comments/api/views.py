from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly


class CommentApiView(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filterset_fields = ['post', 'post__slug']
