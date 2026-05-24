from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/contacts/', include('contacts.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/blog/', include('blog.urls')),
]
