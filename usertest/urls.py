from django.conf.urls import patterns, url

from usertest import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^update/$', views.update_view, name='update'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
)
