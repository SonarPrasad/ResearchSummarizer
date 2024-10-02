from django import forms
from .models import PDFUpload, Question

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['file']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.TextInput(attrs={
                'placeholder': 'Enter your question here...',  # Placeholder text
                'class': 'form',  # Class for styling
                'required': True,  # Make it required
            }),
        }