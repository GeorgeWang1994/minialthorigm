from django.conf.urls.defaults import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^favor/', include('favor.urls')),
    url(r'^like/', include('like.urls')),
    url(r'^comment/', include('comment.urls')),
]
