# pdf_app/views.py

from django.shortcuts import render
from .models import PDF

def pdf_gallery(request):
    pdfs = PDF.objects.all()
    return render(request, 'pdf_app/pdf_gallery.html', {'pdfs': pdfs})
