from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Golfer, Scorecard, Score

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

       

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['hole_number', 'par', 'distance', 'swing_score']

ScoreFormSet = forms.inlineformset_factory(
    Scorecard, Score, form=ScoreForm, extra=18, max_num=18, min_num=9
)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

