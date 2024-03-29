"""arichivo principal punto de entrada a las peticiones en el proyecto y busca la url requerida y trata de encontrarla con su vista correspondiente"""
"""pape URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from papeposts import views
from users import views as users_views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    #path('hello_world/',views.hello_world, name="hello_world"),
    #path('odenados/', views.odenados,name="sort"),
    #path('hello_world/<str:name>/<int:age>', views.hello_world)
	
	path('', include(('papeposts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)