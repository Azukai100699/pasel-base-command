from django.contrib import admin
from django.urls import path, include  # <-- Added 'include' here
from django.conf import settings
from django.conf.urls.static import static
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('leadership/', views.directors, name='directors'),
    path('register/', views.register, name='register'),
    path('hub/<int:hub_id>/', views.hub_detail, name='hub_detail'),
    
    # ADDED THIS LINE: Activates Django's built-in login & logout URLs
    path('accounts/', include('django.contrib.auth.urls')),
]

# This ensures your Director profile photos render correctly
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)