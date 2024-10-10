# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import KnowledgeLevel
from .serializers import KnowledgeSerializer



class SkillAssessmentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        # Dummy implementation of a quiz grading system (ML model can be integrated here)
        answers = request.data.get('answers')
        score = sum(answers)  # Example calculation

        user.initial_score = score
        user.save()

        return Response({'score': score})

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'username': user.username,
            'email': user.email,
            'interests': user.interests,
            'initial_score': user.initial_score,
        }
        return Response(data)

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import KnowledgeSerializer

class KnowledgeView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view

    def post(self, request):
        if request.user.is_anonymous:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        print('Incoming request data:', request.data)  # Debugging print
        serializer = KnowledgeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)  # Pass the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print('Validation errors:', serializer.errors)  # Debugging print for validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)