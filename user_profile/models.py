from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gensel=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

selspecies=(
    ('whale','whale'),
    ('Basking','Basking'),
    ('Shortfin mako','Shortfin mako'),
    ('thresher','thresher'),
    ('Bull','Bull'),
    ('Tiger','Tiger'),
    ('White','White'),
    ('Oceanic Whitetip','Oceanic Whitetip'),
    ('Hammerhead','Hammerhead'),
    ('Nurse','Nurse'),
    ('Blacktip reef','Blacktip reef'),
    ('sand tiger','sand tiger'),
    ('Lemon','Lemon'),
    ('Brownbanded Bamboo','Brownbanded Bamboo'),
    ('Megamouth','Megamouth'),
)

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.IntegerField()
    gender=models.CharField(max_length=10, choices=gensel)
    age=models.IntegerField()
    address=models.CharField(max_length=30)
    Species=models.CharField(max_length=30, choices=selspecies, default='whale')

    def __str__(self):
        return self.user.username
