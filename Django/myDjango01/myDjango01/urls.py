"""
URL configuration for myDjango01 project.

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
from django.urls import path
from myapp01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list),
    path('write_form/', views.write_form),
    path('insert/', views.insert),
    path('list/', views.list),
    path('detail_idx/', views.detail_idx),
    path('detail/<int:board_idx>', views.detail) # detail/1 과 같은 형태의 의미(REST API 형태의 주소 받기)
]
