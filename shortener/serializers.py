from rest_framework import serializers


class ShortenerSerializer(serializers.Serializer):
    long_url = serializers.URLField()
