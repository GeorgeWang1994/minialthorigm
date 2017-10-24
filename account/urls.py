from django.conf.urls.defaults import url

from account import views as account_view

urlpatterns = [
    url(r'^/(?P<user_id>[^/]+)/detail/$', account_view.detail_view),
    url(r'^/(?P<user_id>[^/]+)/favors/$', account_view.user_favors_view),
    url(r'^/(?P<user_id>[^/]+)/comments/$', account_view.user_comments_view),
]
