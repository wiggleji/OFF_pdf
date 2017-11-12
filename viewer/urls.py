from django.conf.urls import url
from django.conf import settings


from . import views

urlpatterns = [
    # viewer
    url(r'$', views.mag_list,),
]
