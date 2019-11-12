"""example3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('app/',LoginView.as_view(template_name="admin.html"),name="admin"),
    path('home/',TemplateView.as_view(template_name="home.html"),name="home"),
    path('organisation/',TemplateView.as_view(template_name="org.html"),name="organisation"),
    path('faqs/',TemplateView.as_view(template_name="faqs.html"),name="faqs"),
    path('donar/',TemplateView.as_view(template_name="doner.html"),name="doner"),

]
