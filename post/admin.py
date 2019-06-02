from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'created_on', 'published']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'text']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)
