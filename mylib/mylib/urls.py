
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mylib/', include('cartile.urls')),
    path('admin/', admin.site.urls),
]
