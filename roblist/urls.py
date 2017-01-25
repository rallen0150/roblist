from django.conf.urls import url, include
from django.contrib import admin

from app.views import IndexView, UserCreateView, CategoryCreateView, CategoryListView, \
                      ItemCreateView, CategoryDetailView, ItemDetailView#, ProfileUpdateView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^new_category/$', CategoryCreateView.as_view(), name='category_create_view'),
    url(r'^category/list/$', CategoryListView.as_view(), name='category_list_view'),
    url(r'^category/(?P<pk>\d+)/new_item/$', ItemCreateView.as_view(), name='item_create_view'),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category_detail_view'),
    url(r'^item/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail_view'),
    # url(r'^account/profile/$', ProfileUpdateView.as_view(), name='profile_update_view'),
]
