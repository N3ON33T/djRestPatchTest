# from django.shortcuts import render

from .models import News
from .serializers import NewsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NewsList(APIView):
    # List all News instances (GET) or create a News instance (POST)
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True) # Python Native to JSON
        return Response(serializer.data)
    
    def post(self, request, format=None):
        deserializer = NewsSerializer(data=request.data) # JSON to Python Native
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_201_CREATED)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsDetail(APIView):
    # Retrieve, update, patch or delete a News instance
    def get_object(self, pk): # Get model instance
        try:
            return News.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None): # Retrieve
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None): # Update entire model instance
        news = self.get_object(pk)
        deserializer = NewsSerializer(news, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None): # Update based on partial data
        news = self.get_object(pk)
        deserializer = NewsSerializer(news, data=request.data, partial=True)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        news = self.get_object(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
