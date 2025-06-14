from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("studio.urls")),
    path('admin/', admin.site.urls),
    path('studio/', include('studio.urls')),  # Uncomment if you want to namespace the studio app

]
# here you need to import urls from the studio app, which contains the views for handling class schedules and bookings. undersrood? yess but how to do

"""
URL configuration for booking_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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