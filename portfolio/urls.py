from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^index/$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^research/$', views.research, name='research'),
    url(r'^interests/$', views.interests, name='interests'),
    url(r'^cv/$', views.cv, name='cv'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^project1/$', views.project1, name='project1'),
    url(r'^research1/$', views.research1, name="research1"),
    url(r'^research2/$', views.research2, name="research2"),
]
