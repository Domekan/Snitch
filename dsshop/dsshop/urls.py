"""
URL configuration for dsshop project.

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
from django.urls import path,include
from project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path("", views.index, name='index'),
    path("about.html", views.about_view, name='about'),
    path("blog.html", views.blog_view, name='blog'),
    path("contact.html", views.contact_view, name='contact'),
    path("elements.html", views.elements_view, name='elements'),
    path("index.html", views.index_view, name='index'),
    path("main.html", views.main_view, name='main'),
    path("performer.html", views.performer_view, name='performer'),
    path("Program.html", views.Program_view, name='Program'),
    path("single-blog.html", views.single_blog_view, name='single-blog'),
    path("venue.html", views.venue_view, name='venue'),
    path("index2.html", views.index2_view, name='index2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)