"""AdaptiveCheatSheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact_us/', views.contact_us),
    url(r'^logout/', views.login),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^personal/', views.personal),
    url(r'^addnotes/', views.save_note ),
    url(r'^getnotes/', views.get_notes ),
    url(r'^getnotesbytag/', views.get_notes_bytag),
    url(r'^useractivity/', views.user_activity),
url(r'^/userProfile/counter', views.dashboard),
    url(r'^api/autocomplete/' , views.elastic),

]
