from django.urls import path
from courses.views import HomeListView, index, short_course
from . import views


urlpatterns = [
    path('', views.index),
    path('shortcourses/', views.short_course),
    path('', HomeListView.as_view(), name='home'),
    #path('download/', views.download_pdf_file),
    # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # path('downloadpdf//', views.download_pdf_file, name='download_pdf_file'),

]
