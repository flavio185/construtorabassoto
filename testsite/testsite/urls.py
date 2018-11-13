"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework import routers
from funcionarios.api.viewsets import FuncionarioViewSet

##djangoRESTFramework Lines
router = routers.DefaultRouter()
router.register(r'funcionario', FuncionarioViewSet, base_name="Funcionario")

urlpatterns = [
    #path('', include('notas.urls')),
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('guestbook/', include('guestbook.urls')),
    #path('notas/', include('notas.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('funcionarios_teste/', include('funcionarios_teste.urls')),
    

    # ... the rest of your URLconf goes here ...
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

##djangoRESTFramework Lines
urlpatterns += router.urls