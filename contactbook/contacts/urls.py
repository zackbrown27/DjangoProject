from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='default'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginProcess/$', views.loginProcess, name='loginProcess'),
    url(r'^contacts/$', views.viewContacts, name='contacts'),

]
