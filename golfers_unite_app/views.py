from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

# Render index.html
def index(request):
    return render(request, 'golfers_unite_app/index.html')

# Handle user signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after signup
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Handle user login
def login_view(request):
    if request.method == 'POST':
        # This is assuming you're using Django's built-in LoginView
        # You can customize this logic as needed
        return LoginView.as_view()(request)
    else:
        # Render the login form
        return render(request, 'login.html')  # Replace 'login.html' with your actual login template
