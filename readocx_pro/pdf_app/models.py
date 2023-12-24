from django.db import models

class PDF(models.Model):
    name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name
