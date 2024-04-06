from django.db import models
from django.contrib.auth.models import User

class Golfer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    handicap = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username

class Scorecard(models.Model):
    golfer = models.ForeignKey(Golfer, on_delete=models.CASCADE)
    date_played = models.DateField()
    course_name = models.CharField(max_length=100)
    score = models.PositiveIntegerField()
    par = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.golfer.user.username}'s Scorecard - {self.date_played}"
