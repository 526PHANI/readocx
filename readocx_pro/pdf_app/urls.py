# pdf_app/urls.py

from django.urls import path
from .views import pdf_gallery

urlpatterns = [
    path('pdf_gallery/', pdf_gallery, name='pdf_gallery'),
]
