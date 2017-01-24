from django.conf.urls import url, include
from django.contrib import admin

from app.views import IndexView, UserCreateView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
]
