from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Sisekelo import settings
from django.conf import settings

admin.site.site_header = 'Sisekelo Admin'
admin.site.index_title = 'Sisekelo Management System'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('application/', include('applications.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('account/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
#  ]
# if settings.DEVEL:
#         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



