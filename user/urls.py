from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views  import (
    index,
    users_list,
    create_post,
    edit_post,
    post_details,
    PostDetailSlugView,
    delete_post,
    add_comment,
    posts,
)

urlpatterns = [
    path('', index, name='index'),
    path('users_list/', users_list, name='users_list'),
    path('create_post/', create_post, name='create_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('post_details/<int:post_id>/', post_details, name='post_details'),
    path('post/<slug>/', PostDetailSlugView.as_view(), name='post_details_slug'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('add_to_fetured/<int:post_id>/', views.add_to_fetured , name='add_to_fetured'),
    path('remove_from_fetured/<int:post_id>/', views.remove_from_fetured , name='remove_from_fetured'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('posts/', posts, name='posts'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
