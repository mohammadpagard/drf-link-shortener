from rest_framework import serializers
from .models import LinkShortener


class ShortenerSerializer(serializers.Serializer):
    long_url = serializers.URLField()


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkShortener
        fields = '__all__'
