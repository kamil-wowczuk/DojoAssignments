from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^process_money$', views.process),
    url(r'^process_money/(?P<building>[\w]+)$', views.process),
    url(r'^reset$', views.reset)
]
