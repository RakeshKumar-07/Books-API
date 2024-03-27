# urls.py
from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('api/books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/books/<str:isbn>/', BookRetrieveUpdateDeleteAPIView.as_view(), name='book-retrieve-update-delete'),
]
