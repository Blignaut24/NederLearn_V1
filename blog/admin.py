from django.contrib import admin
from .models import Blogpost
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Blogpost)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
