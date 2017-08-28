from django.conf.urls import url, include
import views

projects_urlpatterns = [
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects_ethu/$', views.project_ethu, name='projects_ethu'),
    url(r'^projects_learnpar/$', views.project_learnpar, name='projects_learnpar'),
    url(r'^projects_treeme/$', views.project_treeme, name='projects_treeme'),
    url(r'^projects_cmf/$', views.project_cmf, name='projects_cmf'),
    url(r'^projects_ureveal/$', views.project_ureveal, name='projects_ureveal'),
    url(r'^projects_tune/$', views.project_tune, name='projects_tune'),
    url(r'^research/$', views.research, name='research'),
    url(r'^interests/$', views.interests, name='interests'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^research1/$', views.research1, name="research1"),
    url(r'^research2/$', views.research2, name="research2"),
    url(r'^send_email/$', views.send_email, name="send_email"),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()