from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('recipes_api.urls')),            # API urls
    path('api/', include('recipes.urls')),
    
]
