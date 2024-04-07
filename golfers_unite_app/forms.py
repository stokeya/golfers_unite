from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Golfer, Scorecard

class SignUpForm(UserCreationForm):
    age = forms.IntegerField(required=False)
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'age')

    def save(self, commit=True):
        user = super().save(commit=False)
        age = self.cleaned_data.get('age')
        if commit:
            user.save()
            # Create Golfer instance and link it to the user
            golfer = Golfer.objects.create(user=user, age=age)
        return user

class ScorecardForm(forms.ModelForm):
    class Meta:
        model = Scorecard
        fields = ['course_name', 'score', 'par', 'holes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['holes'].widget = forms.Select(choices=[(9, '9 Holes'), (18, '18 Holes')])