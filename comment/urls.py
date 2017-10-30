from django.conf.urls.defaults import url

from comment import views as comment_view

urlpatterns = [
    url(r'^add/$', comment_view.add_comment_post_view),
    url(r'^delete/$', comment_view.del_comment_post_view),
]
