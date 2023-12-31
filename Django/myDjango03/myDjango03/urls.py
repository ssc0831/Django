"""
URL configuration for myDjango02 project.

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
from django.contrib.auth import views as auth_views
from myapp03 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list),
    path('', views.list),
    path('write_form/', views.write_form),
    path('insert/', views.insert),
    path('detail/<int:board_id>/', views.detail),

    path('comment_insert/', views.comment_insert),

    # WordCloud #
    path('wordcloud/', views.wordcloud),
    path('wordcloud2/', views.wordcloud2),

    # Melon #
    path('melon/', views.melon),

    # Map #
    path('map/', views.map),

    # MovieChart #
    path('movie_chart/', views.movie_chart),
    path('movie/', views.movie),
    path('movie_dbchart/', views.movie_dbchart),

    # Weather #
    path('weather/', views.weather),

   #### Login, LogOut Authentication ####
    path('login/',
         auth_views.LoginView.as_view(template_name='common/login.html'),
         name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),         
    path('signup/', views.signup),
]
