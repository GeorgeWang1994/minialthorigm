from django.conf.urls.defaults import url

from favor import views as favor_view

urlpatterns = [
    url(r'^add/$', favor_view.favor_post_view),
    url(r'^delete/$', favor_view.un_favor_post_view),
]
