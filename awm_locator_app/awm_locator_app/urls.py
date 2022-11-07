"""awm_locator_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from location_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.new_user_registration, name='register_user'),
    path('user_logout/', views.user_logout, name='userlogout'),
    path('logout/', TemplateView.as_view(template_name='user_forms/logout.html'), name='logout'),
    path('menu/', TemplateView.as_view(template_name='user_menu.html'), name='menu'),
    path('register_success/', TemplateView.as_view(template_name='user_forms/register_success.html'), name='register_success'),
    path('map/', TemplateView.as_view(template_name='view_map.html'), name='map'),
    path('update/', views.update_location, name="update_location"),


]
