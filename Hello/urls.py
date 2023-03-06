from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('home.urls'))
]


admin.site.site_header = "Harry Ice-Cream Admin"
admin.site.site_title = "Harry Ice-Cream Portal"
admin.site.index_title = "Welcome to Harry Ice-Cream Researcher Portal"