from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('base.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt'))
]
