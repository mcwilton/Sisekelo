from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    #path('download/', views.download_pdf_file),
    # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # path('downloadpdf//', views.download_pdf_file, name='download_pdf_file'),

]
