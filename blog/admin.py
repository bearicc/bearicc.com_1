from django.contrib import admin
from .models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
