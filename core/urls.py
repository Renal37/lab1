from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about/',include('about.urls')),
    path('contacts/', include('contacts.urls')),
]
