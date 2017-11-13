from django.conf.urls import url
from django.conf import settings


from . import views

urlpatterns = [
    # viewer
    url(r'^viewer/(?P<pk>\d+)/$', views.mag_detail, name='viewer'),
    url(r'$', views.mag_list,),
]
