"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as blogs_v
urlpatterns = [
    path('', blogs_v.start,name='start'),
    path('home/', blogs_v.home,name='home'),
    path('home/add', blogs_v.post_add,name='add'),
    url(r'^home/(?P<id>\d+)/$',blogs_v.content,name='content'),
    url(r'^home/(?P<id>\d+)/delete/$',blogs_v.delete,name='delete'),
    path('about/', blogs_v.about,name='about'),
    path('contact/', blogs_v.TheContact,name='TheContact'),
    path('register/', blogs_v.register,name='register'),
    path('login/', blogs_v.login_view,name='login'),
    path('logout/', blogs_v.logout_view,name='logout'),
    path('admin/', admin.site.urls),

]
if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)