from django.conf.urls import include, url

from .views import flow, storyboard

urlpatterns = [
    url(r'^dropbox-auth-start/?$', flow.dropbox_auth_start, name='dropbox_auth_start'),
    url(r'^dropbox-auth-finish$', flow.dropbox_auth_finish, name='dropbox_auth_finish'),
    url(r'^logout$', flow.logout, name='logout'),


    url(r'^$', flow.home, name='home'),
    url(r'^story/(?P<slug>[\w\d]+)$', storyboard.story),
    url(r'^story$', storyboard.all_story),
]