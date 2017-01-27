from django.conf.urls import include, url
from django.contrib import admin

from flow import views
    # Examples:
    # url(r'^$', 'dboauth2flow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dropbox-auth-start/?$', views.dropbox_auth_start, name='dropbox_auth_start'),
    url(r'^dropbox-auth-finish$', views.dropbox_auth_finish, name='dropbox_auth_finish'),
    url(r'^$', views.home, name='home'),
    url(r'^logout$', views.logout, name='logout')


]
