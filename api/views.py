from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Author
from .serializers import BookListSerializer, AuthorListSerializer, BookSerializer, AuthorDetailSerializer

# Create book list view with serializers
class BookListView(APIView):
    def get(self, request):

        books = Book.objects.order_by('title')
        result = BookListSerializer(books, many = True)

        return Response(result.data, status = status.HTTP_200_OK)

    def post(self, request):
        result = BookSerializer(data = request.data)

        if result.is_valid():
            result.save()

            return Response(result.data, status = status.HTTP_201_CREATED)
        
        return Response(result.errors, status = status.HTTP_400_BAD_REQUEST)

# Create detail book view
class BookDetailView(APIView):
    def get_book(self, id):
        try:
            return Book.objects.get(id = id)
        except Book.DoesNotExist:
            return HttpResponse(status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, book_id):
        book = self.get_book(book_id)
        result = BookSerializer(book)

        return Response(result.data, status = status.HTTP_200_OK)

    def put(self, request, book_id):
        book = self.get_book(book_id)
        result = BookSerializer(book, data = request.data)

        if result.is_valid():
            result.save()

            return Response(result.data, status = status.HTTP_201_CREATED)

        return Response(result.errors, status = status.HTTP_400_BAD_REQUEST)

# Create author list view
class AuthorListView(APIView):
    def get(self, request):
        authors = Author.objects.order_by('fullname')
        result = AuthorListSerializer(authors, many = True)

        return Response(result.data, status = status.HTTP_200_OK)

# Create author detail view
class AuthorDetailView(APIView):
    def get(self, request, author_id):
        author = Author.objects.get(id = author_id)
        result = AuthorDetailSerializer(result)

        return Response(result.data, status = status.HTTP_200_OK)
