from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone

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
    
class GolfCourse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class GolferAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'handicap', 'age')  # Customize displayed fields
    search_fields = ('user__username', 'user__email')  # Add search functionality

admin.site.register(Golfer, GolferAdmin)
