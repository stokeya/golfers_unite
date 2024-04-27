from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from django import forms

class Golfer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    handicap = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Scorecard(models.Model):
    golfer = models.ForeignKey(Golfer, on_delete=models.CASCADE)
    date_played = models.DateField(default=timezone.now)
    course_name = models.CharField(max_length=100)
    score = models.PositiveIntegerField()
    par = models.PositiveIntegerField()
    holes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.golfer.user.username}'s Scorecard - {self.date_played}"

class Score(models.Model):
    scorecard = models.ForeignKey('Scorecard', on_delete=models.CASCADE, related_name='scores')
    hole_number = models.PositiveIntegerField()
    par = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()
    swing_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.scorecard} - Hole {self.hole_number}"

class GolferAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'handicap', 'age')
    search_fields = ('user__username', 'user__email')

admin.site.register(Golfer, GolferAdmin)
