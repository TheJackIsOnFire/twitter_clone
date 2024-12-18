import debug_toolbar
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    re_path('twitter/(?P<version>(v1|v2))/', include('users.urls')),
    re_path('twitter/(?P<version>(v1|v2))/', include('login.urls')),
    re_path('twitter/(?P<version>(v1|v2))/', include('post_tweets.urls')),
    re_path('twitter/(?P<version>(v1|v2))/', include('feed_tweets.urls')),
]