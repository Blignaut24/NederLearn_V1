# ---------------------
# Django Imports
# ---------------------
# Standard library imports
from django.views import generic
from .models import Blogpost, Comment, MediaCategory

# ---------------------
# BlogPostList View
# ---------------------
# This class-based view lists all blogposts, ordered by creation date.
# Only blogposts with status=1 (published) are shown.
# Pagination is set to display 6 posts per page.
class BlogPostList(generic.ListView):

    # Define the model
    model = Blogpost

    # Define the queryset
    queryset = Blogpost.objects.filter(status=1).order_by('created_on')
    context_object_name = 'blogposts'

    # Define the template
    template_name = 'index.html'

    # Set pagination
    paginate_by = 6
