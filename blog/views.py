# Standard library imports
# from django.shortcuts import render
from django.views import generic
from .models import Blogpost, Comment, MediaCategory

# ---------------------
# Create your views here.
# ---------------------
class PostList(generic.ListView):
    '''
    This class-based view lists all blogposts, ordered by creation date.
    Only blogposts with status=1 (published) are shown.
    Pagination is set to display 6 posts per page.
    '''
    # Define the model
    model = Blogpost

    # Define the queryset
    queryset = Blogpost.objects.filter(status=1).order_by('created_on')

    # Define the template
    template_name = 'index.html'

    # Set pagination
    paginate_by = 6

