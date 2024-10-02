import os
from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse, HttpResponseNotFound
from .forms import PDFUploadForm, QuestionForm
from .models import PDFUpload
from .ai_tools import get_vector_store, process_user_input, generate_word_content
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """Render the homepage and handle uploads/questions."""
    # Initialize separate messages for each section
    upload_message = None
    word_message = None

    # Fetch uploaded PDFs
    uploaded_pdfs = PDFUpload.objects.all()
    form = QuestionForm()

    # Check if session is active
    if request.session.get('session_active'):
        if request.method == 'POST':
            if 'upload_pdf' in request.POST:
                return upload_pdf(request)
            elif 'ask_question' in request.POST:
                return ask_question(request)
    else:
        if uploaded_pdfs.exists():
            PDFUpload.objects.all().delete()
        request.session['session_active'] = True

    # Get the download link from the session if it exists
    download_link = request.session.pop('download_link', None)

    return render(request, 'home.html', {
        'upload_message': upload_message,
        'word_message': word_message,
        'uploaded_pdfs': uploaded_pdfs,
        'form': form,
        'download_link': download_link,
    })

def upload_pdf(request):
    """Handle PDF upload and process the file."""
    form = PDFUploadForm(request.POST, request.FILES)
    question_form = QuestionForm()  # Create an instance of the QuestionForm

    # Fetch uploaded PDFs
    uploaded_pdfs = PDFUpload.objects.all()

    if form.is_valid():
        pdf_upload = form.save()
        
        # Re-fetch updated list of PDFs after the upload
        uploaded_pdfs = PDFUpload.objects.all()
        
        get_vector_store(uploaded_pdfs)

        upload_message = "PDF uploaded successfully!"
    else:
        print(form.errors)
        upload_message = "There was an error with the upload."

    return render(request, 'home.html', {
        'upload_message': upload_message,
        'uploaded_pdfs': uploaded_pdfs,
        'form': question_form,  # Pass the QuestionForm to the template
    })

def ask_question(request):
    """Handle question asking and return the AI response."""
    form = QuestionForm(request.POST)
    answer = None
    question_text = None

    if form.is_valid():
        question = form.save()  # Save the question form
        question_text = question.question_text  # Get the submitted question text
        answer = process_user_input(question_text)  # Get the AI response
        question.answer_text = answer  # Assign the answer to the question object
        question.save()  # Save the question with the answer

    # Fetch uploaded PDFs for display
    uploaded_pdfs = PDFUpload.objects.all()  
    return render(request, 'home.html', {
        'form': QuestionForm(),  # Reset form to allow new question input
        'answer': answer,  # Include the AI response
        'question': question_text,  # Include the last question
        'uploaded_pdfs': uploaded_pdfs,  # Pass uploaded PDFs to the template
        'last_question': question_text,  # Pass the last question to the template
    })

def create_word(request):
    """Handle Word file creation and return the homepage with updated context."""
    word_message = None

    # Fetch uploaded PDFs
    uploaded_pdfs = PDFUpload.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        user_input = request.POST.get('user_input')

        if title and user_input:
            file_path = generate_word_content(title, user_input)
            word_message = "Word file created successfully!"
            return render(request, 'home.html', {
                'word_message': word_message,
                'uploaded_pdfs': uploaded_pdfs,
                'form': QuestionForm(),
                'download_link': os.path.basename(file_path),
                'scroll_to': 'word-section'
            })

    return render(request, 'home.html', {
        'word_message': word_message,
        'uploaded_pdfs': uploaded_pdfs,
        'form': QuestionForm(),
    })

def download_file(request, file_name):
    file_path = os.path.join(settings.BASE_DIR, 'generated_files', file_name)
    
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        return HttpResponseNotFound("File not found")

def about(request):
    """Render the 'About' page."""
    return render(request, 'about.html')