from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^cv/$', views.cv, name='cv'),
    url(r'^contact/$', views.contact, name='contact'),
]
