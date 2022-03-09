from django.contrib import admin
from .models import *
# Register your models here.


class TagTublerInline(admin.TabularInline):
    model = Tag


class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]
    #for tabular form show in database
    list_display = ['title', 'author', 'date', 'status', 'section', 'Main_post']
    list_editable = ['status', 'section', 'Main_post']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
