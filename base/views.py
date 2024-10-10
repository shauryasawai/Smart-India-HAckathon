# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

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
