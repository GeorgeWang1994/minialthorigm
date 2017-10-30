from django.conf.urls.defaults import url

from tag import views as tag_view

urlpatterns = [
    url(r'^post/add/$', tag_view.create_post_tag_view),
    url(r'^post/delete/$', tag_view.del_post_tag_view),
]