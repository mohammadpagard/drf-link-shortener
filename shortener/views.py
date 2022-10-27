# Django packages
from django.shortcuts import get_object_or_404, redirect
# DRF Packages
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Local apps
from .models import LinkShortener
from .serializers import ShortenerSerializer, LinksSerializer


class ShortenerView(APIView):
    def get(self, request, short_url):
        short_url = get_object_or_404(LinkShortener, active=True, short_url=short_url)
        return redirect(short_url.long_url)


class LinkShortenerView(APIView):
    serializer_class = ShortenerSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ser_data = self.serializer_class(data=request.POST)
        if ser_data.is_valid():
            ser_validate_data = ser_data.validated_data
            LinkShortener.create_short_url(long_url=ser_validate_data.get('long_url'))
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        links = LinkShortener.objects.all()
        serializer_data = LinksSerializer(instance=links, many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)
