from django.db import models
import uuid

# Create your API models here.

# Create author model
class Author(models.Model):
    id = models.CharField(default = uuid.uuid4().hex, primary_key = True, max_length = 200, unique = True)
    fullname = models.CharField(max_length = 100, null = False)
    biography = models.TextField(max_length = 600)
    age = models.IntegerField()
    created_at = models.DateField(auto_now_add = True)
    birthday = models.DateTimeField()
    image = models.ImageField(verbose_name = 'Image', upload_to = 'authors/images/', default = 'authors/images/noimage.png')
    # books = 

    def __str__(self):
        return self.fullname

    def snippet(self):
        return self.about[:17] + '...'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

# Create book model
class Book(models.Model):
    id = models.CharField(default = uuid.uuid4().hex, primary_key = True, max_length = 200, unique = True)
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 600)
    created_at = models.DateTimeField(auto_now_add = True)
    published_at = models.DateTimeField()
    bookImg = models.ImageField(default = 'books/images/noimage.png', upload_to = 'books/images/')
    rating = models.DecimalField(decimal_places = 1, max_digits = 5, null = True)
    price = models.FloatField(null = False, default = 0)
    draft = models.BooleanField(default = True, null = False)
    author = models.ForeignKey(Author, default = None, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.title[:42] + '...'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'