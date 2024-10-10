# urls.py
from django.urls import path,include
from .views import SkillAssessmentView,UserProfileView  
from . import views
from .views import KnowledgeView



urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('skill-assessment/', SkillAssessmentView.as_view(), name='skill-assessment'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('knowledge/', KnowledgeView.as_view(), name='knowledge'),

]
