"""homesolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import HomeTemplateView
from contact.views import ContactFormView, ContactSuccessView

app_name='homesolutions'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplateView.as_view(), name='home'),
    # path('getstarted/', include('contact.urls', namespace='contact')),
    path('getstarted/', ContactFormView.as_view(), name='contact'),
    # path('contact/', include('contact.urls')),
    # path('contactview/', ContactFormView.as_view(), name='contact'),
    path('success/', ContactSuccessView.as_view(), name='contactsuccess'),
]

admin.site.site_header = ("HSS Site Administration")
admin.site.site_title = ("HSS Site Admin")