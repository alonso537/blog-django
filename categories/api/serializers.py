from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):

    # posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
