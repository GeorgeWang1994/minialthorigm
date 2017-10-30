from django.conf.urls.defaults import url

from chat import views as chat_view

urlpatterns = [
    url(r'^last/list/$', chat_view.home_view),
    url(r'^hot/list/$', chat_view.hot_post_view),
    url(r'^create/$', chat_view.create_post_view),
    url(r'^delete/$', chat_view.del_post_view),
    url(r'^(?P<post_id>[^/]+)/detail/$', chat_view.get_post_view),
]
