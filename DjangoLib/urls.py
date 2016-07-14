from django.conf.urls import include, url
from django.contrib import admin

import library.urls

urlpatterns = [
    url(r'^$', include(library.urls)),
    url(r'^index/', include(library.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
