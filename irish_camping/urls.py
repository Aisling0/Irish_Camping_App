"""irish_camping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from accounts import views as accounts_views
from home import views as home_views
from threads import views as forum_views
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^about/$', home_views.about, name='about'),

    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # Forum URLs
    url(r'^forum/$', forum_views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$',
        forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$',
        forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$',
        forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$',
        forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',
        forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',
        forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$',
        forum_views.thread_vote, name='cast_vote'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

]

# if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
#   ]+urlpatterns
