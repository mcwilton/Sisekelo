from django.urls import path
from courses.views import HomeListView,  accredited_program, index
from . import views


urlpatterns = [
    path('', views.index),
    path('shortcourses/', views.accredited_program),
    # path('', HomeListView.as_view(), name='home'),
    #path('download/', views.download_pdf_file),
    # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # path('downloadpdf//', views.download_pdf_file, name='download_pdf_file'),

]
