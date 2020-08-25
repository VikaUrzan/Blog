from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug', 'created_at', 'get_photo', 'category', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    readonly_fields = ('views', 'get_photo', 'created_at')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src = "{obj.photo.url}" width = "50">')
        return '-'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
