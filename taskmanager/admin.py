from django.contrib import admin
from.models import *
# Register your models here.


admin.site.register(Project)
admin.site.register(Task)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
