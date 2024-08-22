from django.contrib import admin
from posts.models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'category', 'created_at', 'updated_at')
    list_editable = ('rate', 'category')
    list_display_links = ('id', 'title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'category', 'tag')
    search_fields = ('title', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

