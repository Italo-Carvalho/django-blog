from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("blog_images", views.display_images, name="blog_images"),
    path("drafts/", views.post_draft_list, name="post_draft_list"),
    path("post/<pk>/publish/", views.post_publish, name="post_publish"),
    path("post/<pk>/remove/", views.post_remove, name="post_remove"),
    path("post/<int:pk>/comment/", views.post_detail, name="views.post_detail"),
    path("comment/<int:pk>/approve/", views.comment_approve, name="comment_approve"),
    path("comment/<int:pk>/remove/", views.comment_remove, name="comment_remove"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
