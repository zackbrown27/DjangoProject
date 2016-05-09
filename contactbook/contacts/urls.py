from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='default'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^loginProcess/$', views.loginProcess, name='loginProcess'),
    url(r'^contacts/', views.viewContacts, name='contacts'),
    url(r'^contactsbyfname/', views.viewContactsByFName, name='contacts'),
    url(r'^contactsbylname/', views.viewContactsByLName, name='contacts'),
    url(r'^contactsbypnumber/', views.viewContactsByPNumber, name='contacts'),
    url(r'^contactsbyemail/', views.viewContactsByEmail, name='contacts'),
    url(r'^contact/([0-9]*)', views.saveContact, name='contact'),
    url(r'^contactus/$', views.contactUs, name='contact'),
	url(r'^delete/(?P<contact_id>[0-9]+)/$', views.deleteContact, name='delete'),
    url(r'^addcontact/', views.saveContact, name='add'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^loginProcess/$', views.loginProcess, name='loginProcess'),

]
