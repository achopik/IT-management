from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('management.urls')),
    path('auth/', include('registration.urls'))
]
