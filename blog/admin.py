from django.contrib import admin
from.models import Blogpost
from.models import MediaCategory
from.models import UserProfile
from.models import Comment

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(MediaCategory)
admin.site.register(UserProfile)
admin.site.register(Comment)
