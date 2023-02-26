from rest_framework import serializers

from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
