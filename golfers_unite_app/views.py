from datetime import date
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView as BaseLoginView
from .forms import SignUpForm, ScorecardForm, LoginForm, ScoreForm, ScoreFormSet
from .models import Golfer, Scorecard, Score
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .decorators import *

class CustomLoginView(BaseLoginView):
    template_name = 'golfers_unite_app/login.html'

# Render index.html
def index(request):
    return render(request, 'golfers_unite_app/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create the golfer profile
            golfer = Golfer.objects.create(user=user)

            # Get the number of holes selected by the user
            holes = int(request.POST.get('holes', 9))

            # Create initial scorecard for the golfer
            scorecard = Scorecard.objects.create(golfer=golfer, date_played=date.today(), course_name='Initial Course', score=0, par=0, holes=holes)

            # Log the user in after signup
            login(request, user)

            return redirect('golfers_unite_app/index')  # Redirect to the homepage after successful signup
    else:
        form = SignUpForm()
    return render(request, 'golfers_unite_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')  # Redirect to the welcome page
            else:
                # Add an error message if authentication fails
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'golfers_unite_app/login.html', {'form': form})

@login_required
def welcome_view(request):
    # Get the currently logged-in user
    user = request.user
    return render(request, 'golfers_unite_app/welcome.html', {'user': user})

def active_golfers_view(request):
    # Retrieve all golfers from the database
    golfers = Golfer.objects.all()
    # Pass the retrieved golfers to the template for rendering
    return render(request, 'golfers_unite_app/active_golfers.html', {'golfers': golfers})

# Remove one of the add_scorecard functions or rename it
def add_scorecard(request, golfer_id):
    if request.method == 'POST':
        form = ScorecardForm(request.POST)
        if form.is_valid():
            # Save the scorecard
            scorecard = form.save(commit=False)
            scorecard.golfer_id = golfer_id
            scorecard.save()
            return redirect('active_golfers')  # Redirect to a suitable URL
    else:
        form = ScorecardForm()
    return render(request, 'golfers_unite_app/add_scorecard.html', {'form': form})

def edit_scorecard(request, scorecard_id):
    scorecard = get_object_or_404(Scorecard, id=scorecard_id)
    if request.method == 'POST':
        form = ScorecardForm(request.POST, instance=scorecard)
        if form.is_valid():
            form.save()
            return redirect('golfers_unite_app/active_golfers')
    else:
        form = ScorecardForm(instance=scorecard)
    return render(request, 'golfers_unite_app/edit_scorecard.html', {'form': form})

def delete_scorecard(request, scorecard_id):
    scorecard = get_object_or_404(Scorecard, id=scorecard_id)
    if request.method == 'POST':
        scorecard.delete()
        return redirect('golfers_unite_app/active_golfers')
    return render(request, 'golfers_unite_app/delete_scorecard.html', {'scorecard': scorecard})


def delete_scorecard(request, scorecard_id):
    scorecard = get_object_or_404(Scorecard, id=scorecard_id)
    if request.method == 'POST':
        scorecard.delete()
        return redirect('active_golfers')  # Redirect to a relevant page after deletion
    return render(request, 'golfers_unite_app/confirm_delete_scorecard.html', {'scorecard': scorecard})

def registerPage(request):
    # Logic for handling registration page request goes here
    return render(request, 'golfers_unite_app/registration/register.html')  # Example template name, adjust as needed

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')  # Redirect to the homepage after logout
    return render(request, 'golfers_unite_app/logout.html')
           
