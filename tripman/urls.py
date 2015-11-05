"""tripman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from core.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', signin),
    url(r'^$', index),
    url(r'^signout', signout),
    url(r'^indexAdmin', indexAdmin),
    url(r'^indexClient', indexClient),
    url(r'^indexDrive', indexDriver),
    url(r'^subIndexUsers', subIndexUsers),
    
    url(r'^subIndexDriverTravels', subIndexDriverTravels),
    
    url(r'^subIndexTravels', subIndexTravels),
    url(r'^addTravel', addTravel),
    
    url(r'^submitReport/(?P<tid>[0-9]+)/$', submitReport, name="submitReport"),
    
    url(r'^approveTravel/(?P<tid>[0-9]+)/$', approveTravel, name="approveTravel"),
    url(r'^removeTravel/(?P<tid>[0-9]+)/$', removeTravel, name="removeTravel"),
    url(r'^viewTravel/(?P<tid>[0-9]+)/$', viewTravel, name="viewTravel"),
    
    url(r'^removePassenger/(?P<tid>[0-9]+)/(?P<pid>[0-9]+)/$', removePassenger, name="removePassenger"),
    url(r'^viewPassengers/(?P<tid>[0-9]+)/$', viewPassengers, name="viewPassengers"),
    
    
    url(r'^viewReport/(?P<tid>[0-9]+)/$', viewReport, name="viewReport"),
    url(r'^viewReportedReport/(?P<tid>[0-9]+)/$', viewReportedReport, name="viewReportedReport"),
    
    url(r'^redirectUser', redirectUser),
    
    url(r'^editDriver', editDriver),
    
    
    url(r'^subIndexReports', subIndexReports),
    url(r'^subIndexVehicles', subIndexVehicles),
    url(r'^addGuestUser', addGuestUser),
    url(r'^addUser', addUser),
    url(r'^removeUser/(?P<uid>[0-9]+)/$', removeUser, name="removeUser"),
    url(r'^editUser/(?P<uid>[0-9]+)/$', editUser, name="editUser"),
    url(r'^addVehicle', addVehicle),
    url(r'^removeVehicle/(?P<vid>[0-9]+)/$', removeVehicle, name="removeVehicle"),
    url(r'^editVehicle/(?P<vid>[0-9]+)/$', editVehicle, name="editVehicle")
]
