from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, ScorecardForm
from .models import Golfer, Scorecard
from django.shortcuts import get_object_or_404

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

            return redirect('index')  # Redirect to the homepage after successful signup
    else:
        form = SignUpForm()
    return render(request, 'golfers_unite_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # If it's a POST request, delegate the login process to Django's LoginView
        return LoginView.as_view()(request)
    else:
        # If it's a GET request, render the login form
        return render(request, 'login.html')  # Replace 'login.html' with your actual login template
    

def active_golfers_view(request):
    # Retrieve all golfers from the database
    golfers = Golfer.objects.all()
    # Pass the retrieved golfers to the template for rendering
    return render(request, 'golfers_unite_app/active_golfers.html', {'golfers': golfers})

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

def delete_scorecard(request, scorecard_id):
    scorecard = get_object_or_404(Scorecard, id=scorecard_id)
    if request.method == 'POST':
        scorecard.delete()
        return redirect('active_golfers')  # Redirect to a relevant page after deletion
    return render(request, 'golfers_unite_app/confirm_delete_scorecard.html', {'scorecard': scorecard})
    
