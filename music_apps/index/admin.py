from django.contrib import admin
from .models import *
# Register your models here.

# 修改title 和 header
admin.site.site_title = '我的音乐后台管理系统'
admin.site.site_header = '我的音乐'

# 模型Label

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    
    list_display = ['label_id','label_name']
    search_fields = ['label_name']
    ordering = ['label_id']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_id', 'song_name', 'song_singer', 'song_album','song_type','song_time']
    search_fields = ['song_name', 'song_singer']
    list_filter = ['song_name', 'song_singer']
    ordering = ['song_id']

@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ['dynamic_id', 'song','dynamic_plays', 'dynamic_search','dynamic_download']
    search_fields = ['dynamic_id', 'song']
    list_filter = ['dynamic_plays', 'dynamic_search', 'dynamic_download']
    ordering = ['dynamic_id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'comment_text','comment_user', 'comment_date','song']
    search_fields = ['comment_user', 'comment_date','song']
    list_filter = ['comment_user', 'comment_date', 'song']
    ordering = ['comment_date']