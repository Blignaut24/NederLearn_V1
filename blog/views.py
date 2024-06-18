# ---------------------
# Django Imports
# ---------------------
# Standard library imports
# from django.shortcuts import render -The render function in Django is a tool that takes a specific HTML template and information, and uses them to create an HTML page that the user can see in their browser.
from django.views import generic, View
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
    
# ---------------------
# BlogPostDetail View
# ---------------------
# This class-based view displays the details of a single blogpost specified by its slug.
# It also fetches the comments associated with the blogpost and checks if the user has 
# liked the blogpost

class BlogPostDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comments = blogpost.comments.filter(approved=False)\
            .order_by("created_on")
        liked = False
        if blogpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blogpost_detail.html",
            {
                "blogpost": blogpost,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


