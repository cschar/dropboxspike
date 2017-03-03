from django.conf.urls import include, url

from .views import oauth, storyboard

urlpatterns = [
    #auth
    url(r'^dropbox-auth-start/?$', oauth.dropbox_auth_start, name='dropbox_auth_start'),
    url(r'^dropbox-auth-finish$', oauth.dropbox_auth_finish, name='dropbox_auth_finish'),
    url(r'^logout$', oauth.logout, name='logout'),

    url(r'^$', storyboard.home, name='home'),
    url(r'^story/(?P<slug>[\w\d]+)$', storyboard.story_detail),
    url(r'^story$', storyboard.story_list),
]