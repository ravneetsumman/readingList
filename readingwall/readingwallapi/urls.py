from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import WallpostCreate, WallpostDetail, Friends
from rest_framework.authtoken.views import obtain_auth_token
from readingwallapi import views


urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', # ADD THIS URL
                               namespace='rest_framework')),
    url(r'^wallposts/$', WallpostCreate.as_view(), name="create"),
    url(r'^connections/$', views.Friends.as_view()),
    url(r'^wallposts/(?P<pk>[0-9]+)/$',
        WallpostDetail.as_view(), name="details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
