from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='home'),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls'), name='user'),
    path('blog/', views.blog , name='blog'),
    path('blog/<slug>/', views.PostDetailSlugView.as_view(), name='post_details_slug'),
    path('working/', views.working , name='working'),
    path('newsletter/', include('newsletter.urls')),
    path('tinymce/', include('tinymce.urls')),

    path('clatmocks/', views.working, name='clat_mocks'),
    path('most_recent/', views.most_recent, name='most_recent'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms_and_conditions, name='terms'),
    #path('newsletter/', include('newsletter.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns = non_translatable_urlpatterns + i18n_patterns(*translatable_urlpatterns)
