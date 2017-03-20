from django.conf.urls import include, url

import pic.views as v

urlpatterns = [
    url(r'^$', v.index, name='index'),

    #API
    url(r'^upload-pic/?$', v.upload_pic, name='upload_pic'),
    url(r'^upload-gif/?$', v.upload_gif, name='upload_gif'),
    url(r'^scene$', v.scene_list, name='scene_list'),
    url(r'^scene/(?P<scene_id>[\d]+)/submissions$', v.submission_list, name='submission_list'),

]