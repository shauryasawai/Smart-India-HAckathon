# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    interests = models.JSONField(default=list, blank=True)
    INTEREST_CHOICES = [
    ('python', 'Python'),
    ('data_science', 'Data Science'),
    ('machine_learning', 'Machine Learning'),
    ('web_development', 'Web Development'),
    ('ai', 'Artificial Intelligence'),
    ('cloud_computing', 'Cloud Computing'),
    ('cyber_security', 'Cyber Security'),
    ('design', 'Design'),
    ('marketing', 'Marketing'),
    ('finance', 'Finance'),
]
    initial_score = models.IntegerField(default=0)  # Starting score for beginners

    def __str__(self):
        return self.username

