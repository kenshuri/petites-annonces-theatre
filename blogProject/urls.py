"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

import blogApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', blogApp.views.index, name='index'),
    path('add_offer', blogApp.views.add_offer, name='add_offer'),
    path('about', blogApp.views.about, name='about'),
    path('offer/<int:offer_id>', blogApp.views.offer, name='offer'),
    path('update_offer/<int:offer_id>', blogApp.views.update_offer, name='update_offer'),
    path('delete_offer/<int:offer_id>', blogApp.views.delete_offer, name='delete_offer'),
    path('signup/', blogApp.views.signup, name='signup'),
    path('__reload__/', include('django_browser_reload.urls')),
]

htmx_urlpatterns = [
    path('offer_search/', blogApp.views.offer_search, name='offer_search'),
]

urlpatterns += htmx_urlpatterns
