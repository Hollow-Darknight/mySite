from django.contrib import admin
from django.db import models
from django.forms import Textarea

from home.models import Category, Post, Thread


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'author_name',
        'published',
        'created_at',
        'threads_count',
    )

    list_filter = (
        'category__name',
        'published',
    )

    autocomplete_fields = ['category']

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 90})},
    }

    def threads_count(self, obj):
        return Thread.objects.filter(post=obj).count()
    threads_count.short_description = "Fil de discussion"


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    search_fields = ['post__title', 'author_name']
    list_display = (
        'post',
        'author_name',
        'status',
        'moderation_text',
        'created_at',
        'text',
    )

    list_editable = ('status', 'moderation_text')
    list_filter = ('status', )