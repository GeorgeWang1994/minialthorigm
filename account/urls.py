from django.conf.urls.defaults import url

from account import views as account_view

urlpatterns = [
    url(r'^(?P<user_id>[^/]+)/detail/$', account_view.user_detail_view),
    url(r'^(?P<user_id>[^/]+)/create/$', account_view.user_create_posts_and_articles_view),
    url(r'^(?P<user_id>[^/]+)/participate/$', account_view.user_participate_posts_and_articles_view),
    url(r'^(?P<user_id>[^/]+)/favors/$', account_view.user_favors_view),
    url(r'^(?P<user_id>[^/]+)/likes/$', account_view.user_likes_view),
    url(r'^(?P<user_id>[^/]+)/comments/$', account_view.user_comments_view),
]
