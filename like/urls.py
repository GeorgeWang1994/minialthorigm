from django.conf.urls.defaults import url

from like import views as like_view

urlpatterns = [
    url(r'^add/$', like_view.like_post_view),
    url(r'^delete/$', like_view.un_like_post_view),
]
