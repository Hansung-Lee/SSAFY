from django.contrib import admin
from .models import Posting, Comment

# Register your models here.


class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')  # 레코드 개별화면 확인
    list_display = ('id', 'content', 'created_at', 'updated_at')  # 리스트에서 표시할 컬럼
    list_display_links = ('id', 'content')  # 리스트에서 clickable 할 속성


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'posting', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'posting', 'content')


admin.site.register(Posting, PostingModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
