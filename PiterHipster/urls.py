"""PiterHipster URL Configuration

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
from django.urls import path, include
from ph_products.api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('piterhipster/', include('Piter_Hipster.urls'),
         )
]

api_urls = (
    path("products/", ProductListView.as_view()),
    path("products/{id}/", ProductView.as_view()),
    path("categories/", CategoriesListView.as_view()),
)

urlpatterns.append(path('api/', include((api_urls, "API"), namespace="API")))
