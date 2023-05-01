from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'slug', 'status', 'created_on', 'approved')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    actions = ['approve_blog_public']

    def approve_blog_public(self, request, queryset):
        queryset.update(approved=True)




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # summernote_fields = ('body')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_blog_public']

    def approve_blog_public(self, request, queryset):
        queryset.update(approved=True)


# Register your models here.
admin.site.register(Profile)