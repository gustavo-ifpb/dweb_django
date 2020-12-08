"""djmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='users-signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='users-signout'),
    path('signup/', views.UserCreateView.as_view(), name='users-signup'),
    
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movies-detail'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movies-create'),
    path('movies/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movies-update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movies-delete'),
    path('', views.MovieListView.as_view(), name='movies-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
