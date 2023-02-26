from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from posts.api.permissions import IsAdminUserOrReadOnly
from posts.models import Post


class PostApiViewSet(ModelViewSet):
    permission_class = [IsAdminUserOrReadOnly]
    serializer_class = PostSerializer
    # queryset = Post.objects.all()
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']
