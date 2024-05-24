from rest_framework import serializers
from .models import Image, ServiceImage


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ["service", "image", "cover"]


class ImageSerializer(serializers.ModelSerializer):
    # Use serializers.ImageField para campos de upload de arquivos
    Path = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = ["ImageID", "Path"]


