from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

from .views import homepage


admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^$", homepage, name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^account/", include("account.urls"))
)
