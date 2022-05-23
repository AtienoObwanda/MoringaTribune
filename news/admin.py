from django.contrib import admin
from . models import Editor, Article, tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal= ('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(tags)