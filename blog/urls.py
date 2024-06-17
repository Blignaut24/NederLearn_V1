# ---------------------
# Import required modules
# ---------------------
from . import views
from django.urls import path

# ---------------------
# Define URL patterns
# ---------------------
# Each URL pattern is defined and assigned to a specific view function or class-based view.
# In this case, the root URL (empty string) is assigned to the PostList class-based view.
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]
