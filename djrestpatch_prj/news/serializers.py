from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    content = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        # Create new News model instance provided data is valid
        return News.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # Update existing News model instance & return it provided data is valid
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance