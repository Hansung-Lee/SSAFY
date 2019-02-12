from django.contrib import admin
from .models import Article

# Register your models here.

# Customizing
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)


admin.site.register(Article, ArticleAdmin)