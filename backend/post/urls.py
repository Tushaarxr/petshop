from django.urls import path

from . import api

urlpatterns = [
    path('', api.post_list, name='post_list'),
    path('<uuid:pk>/', api.post_detail, name='post_detail'),
    path('<uuid:pk>/like/', api.post_like, name='post_like'),
    path('<uuid:pk>/comment/', api.post_create_comment, name='post_create_comment'),
    path('<uuid:pk>/delete/', api.post_delete, name='post_delete'),
    path('<uuid:pk>/report/', api.post_report, name='post_report'),
    path('profile/<uuid:id>/', api.post_list_profile, name='post_list_profile'),
    path('create/', api.post_create, name='post_create'),
    path('<uuid:pk>/edit/', api.post_edit, name='post_edit'),  # New route for editing posts
    path('trends/', api.get_trends, name='get_trends'),
    path('events/', api.event_list_create, name='event_list_create'),
    path('events/register/<uuid:event_id>/', api.event_register, name='event_register'),
    path('<uuid:pk>/bookmark/', api.bookmark_post, name='post_bookmark'),  # New bookmark route
    path('bookmarks/', api.bookmarked_posts, name='bookmarked_posts'),  # New route to view bookmarks
]
