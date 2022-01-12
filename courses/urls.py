from django.urls import path
from courses.views import HomeListView,  accredited_program, index
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.index),
    path('shortcourses/', views.accredited_program, name='shortcourses'),
    path('courseview/', views.test, name='corseview'),
    path('aprograms/', views.test, name='aprograms'),
    path('corporate/', views.test, name='corporate'),
    path('learnerships/', views.test, name='learnerships')
    # path('', HomeListView.as_view(), name='home'),
    #path('download/', views.download_pdf_file),
    # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # # path('downloadpdf/', views.download_pdf_file, name='download_pdf_file'),
    # path('downloadpdf//', views.download_pdf_file, name='download_pdf_file'),

]
