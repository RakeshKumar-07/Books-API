# serializers.py
from rest_framework import serializers
from .models import Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publication_date', 'isbn', 'description']
        read_only_fields = ['isbn']
        
    def validate_publication_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value

    def create(self, validated_data):
        validated_data.pop('isbn', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('isbn', None)
        return super().update(instance, validated_data)