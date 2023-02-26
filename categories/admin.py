from django.contrib import admin
from categories.models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',  'published']
    list_filter = ['published']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
