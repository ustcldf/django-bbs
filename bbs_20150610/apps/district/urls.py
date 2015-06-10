
from django.conf.urls import include, url
from tastypie.api import Api
from apps.district import views
from apps.district.resource import DistrictResource


api = Api('district')
api.register(DistrictResource())


urlpatterns = [
    url(r'^$', views.DistrictListView.as_view(), name='home'),
    url(r'^create/(?P<tag>.+)/$', views.CreateView.as_view(), name='create'),
    url(r'^deleteDistrict/$', views.deleteDistrict, name='deleteDistrict'),
    url(r'^icon/(?P<name>.+)/$', views.SettingIcon.as_view(), name='Icon'),
]
