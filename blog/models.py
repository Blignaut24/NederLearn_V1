from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Published'))


class Blogpost(models.Model):
    """
    The Blogpost model in the NederLearn application signifies an individual 
    blog post. It encapsulates details such as the post's title, slug, author, 
    creation and update times, main content, a short excerpt, and the status 
    of the post (whether it's a draft or published). 
    It also includes an image for the post, the media category it falls under, 
    and, if relevant, the year of release. Additional features allow users to 
    'like' or 'bookmark' posts. These interactions are modeled through 
    many-to-many relationships with the User model.

    """
    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    media_category = models.ForeignKey('MediaCategory', on_delete=models.CASCADE, related_name='blog_posts')
    release_year = models.IntegerField()
    media_link = models.URLField()
    likes = models.ManyToManyField(User, related_name='blogpost_likes', blank=True)
    bookmarks = models.ManyToManyField(User, related_name='blogpost_bookmarks', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.blog_title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_bookmarks(self):
        return self.bookmarks.count()
