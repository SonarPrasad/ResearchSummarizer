from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate the user after registration
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after successful registration
            else:
                return render(request, 'register.html', {'form': form, 'error': 'Authentication failed. Please try again.'})
        else:
            # If form is not valid, return the form with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            login(request, form.get_user())
            return redirect('home')  # Redirect to home after login
        else:
            # If form is not valid, pass the form errors to the template
            return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials. Please try again.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})