from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Sisekelo import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('application/', include('applications.urls')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

