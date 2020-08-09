from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Book, Author

# Create book serializer for book list
class BookListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field = 'fullname', read_only = True)

    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ['draft']

# Create book serializer with detail information
class BookSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field = 'fullname', read_only = True)

    class Meta:
        model = Book
        fields = '__all__'

# Create author serializer for list and detail info
class AuthorListSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'fullname', 'image', 'biography']

class AuthorDetailSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'