from rest_framework import serializers
from .models import BlogPost

class BlogPostListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing posts (no full content)"""
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'excerpt', 'cover_image_url', 'tags', 'created_at']

class BlogPostDetailSerializer(serializers.ModelSerializer):
    """Full serializer for a single post"""
    class Meta:
        model = BlogPost
        fields = '__all__'
