# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

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

class KnowledgeLevel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Update here
    topic = models.CharField(max_length=100)  # e.g., 'Web Development'
    level = models.CharField(max_length=20, default='Beginner')  

    def __str__(self):
        return f"{self.user.username} - {self.topic} ({self.level})"