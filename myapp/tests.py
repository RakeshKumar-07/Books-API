# tests.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.client.force_authenticate(user=self.user)

        self.book_data = {
            'title': 'Test Book',
            'authors': 'Test Author',
            'publication_date': '2023-01-01',
            'isbn': '1234567890123',
            'description': 'This is a test book.'
        }
        self.book = Book.objects.create(**self.book_data)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_book(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_details(self):
        response = self.client.get(f'/api/books/{self.book.isbn}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        updated_data = {
            'title': 'Updated Test Book',
            'authors': 'Updated Test Author',
            'publication_date': '2023-02-02',
            'description': 'This is an updated test book.'
        }
        response = self.client.put(f'/api/books/{self.book.isbn}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.isbn}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
