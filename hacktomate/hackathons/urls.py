from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from hacktomate import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('up/<int:id>', views.up, name='up'),
    path('down/<int:id>', views.down, name='down'),
    path('hackathons/', views.hackathons, name='hackathons'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
