import os
from django.db import models

class PDFUpload(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        base_name = os.path.basename(self.file.name)
        return os.path.splitext(base_name)[0] 
    
class Question(models.Model):
    question_text = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)
    answer_text = models.TextField(blank=True, null=True)
    pdf_upload = models.ForeignKey(PDFUpload, on_delete=models.CASCADE, related_name='questions', null=True)
    
    def __str__(self):
        return self.question_text