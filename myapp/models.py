# models.py
from django.db import models
import uuid

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publication_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = self.generate_isbn()
        super().save(*args, **kwargs)

    def generate_isbn(self):
        unique_id = uuid.uuid4()
        
        isbn = str(unique_id).replace('-', '')[:13]
        
        return isbn
