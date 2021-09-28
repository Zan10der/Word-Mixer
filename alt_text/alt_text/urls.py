from django.contrib import admin
from django.urls import path, include
from scrabble import urls as scrabble_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(scrabble_urls))
]
