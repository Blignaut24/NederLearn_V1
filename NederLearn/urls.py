# ---------------------
# Import Django modules
# ---------------------
from django.contrib import admin
from django.urls import path, include

# ---------------------
# Define URL patterns
# ---------------------
# Each URL pattern is defined and connected to the corresponding view. When a URL is requested, Django will execute the corresponding view function.
urlpatterns = [
    # Add admin site URL
    path('admin/', admin.site.urls),
    # Add blog URLs
    path("", include("blog.urls"), name="blog-urls"),
    # Add summernote URL
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
]
