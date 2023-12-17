"""
URL configuration for ad_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from auth_users.views import CustomLoginView, ResetPasswordView, profile, ChangePasswordView, TemplateView #, AdsList
from django.contrib.auth import views as auth_views
from auth_users.forms import LoginForm
from django.contrib.auth.decorators import login_required
from .views import simple_upload, WorkerList, WorkerDetails, chart_json

urlpatterns = [
    path('analizator/', login_required(simple_upload), name='analizator'),
    path('dashboard/', login_required(TemplateView.as_view(template_name='flatpages/charts.html')), name='dashboard'),
    path('upload/', login_required(simple_upload), name='upload'),
    path('worker/', login_required(WorkerList.as_view(template_name='person_list.html')), name='workers'),
    path('worker/<int:pk>', WorkerDetails.as_view(), name='details'),
    path('', login_required(WorkerList.as_view(template_name='main.html')), name='main'),
    path('worker/<int:pk>/chart/', chart_json, name='chart'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
