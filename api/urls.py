from django.urls import path

from .views import BookListView, AuthorListView, BookDetailView, AuthorDetailView

urlpatterns = [
    path('books', BookListView.as_view()),
    path('books/<slug:book_id>', BookDetailView.as_view()),
    path('authors', AuthorListView.as_view()),
    path('authors/<slug:author_id>', AuthorDetailView.as_view())
]