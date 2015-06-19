from django.contrib import admin
from .models import Post, Category, Comment


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 3


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, CommentInline]

admin.site.register(Post, PostAdmin)
