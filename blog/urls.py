# ---------------------
# Import relevant modules
# ---------------------
from . import views
from django.urls import path

# ---------------------
# Define URL patterns
# ---------------------
# URL pattern for the home page is defined here. When the home route is accessed, the PostList view is rendered.
urlpatterns = [
    path("", views.BlogPostList.as_view(), name="home"),
]
