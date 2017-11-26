from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^containers/', include('containers.urls')),
    url(r'^admin/', admin.site.urls),
]
