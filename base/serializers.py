# serializers.py
from djoser.serializers import UserCreateSerializer
from .models import CustomUser,KnowledgeLevel
from rest_framework import serializers



class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('username', 'password', 'email', 'interests')

from rest_framework import serializers
from .models import KnowledgeLevel

class KnowledgeSerializer(serializers.Serializer):
    # Expect 'knowledge_levels' as the key from the frontend
    knowledge_levels = serializers.JSONField()
    
    
    def create(self, validated_data):
        user = self.context['request'].user  # Get the authenticated user
        knowledge_data = validated_data.get('knowledge_levels', {})
        
        if not isinstance(knowledge_data, dict):
            raise serializers.ValidationError("knowledge_levels must be a dictionary of topics and levels.")
        
        for topic, level in knowledge_data.items():
            if not isinstance(topic, str) or not isinstance(level, str):
                raise serializers.ValidationError("Both topics and levels must be strings.")
            if topic.strip() == '' or level.strip() == '':
                raise serializers.ValidationError("Topic and level cannot be empty.")
            
        KnowledgeLevel.objects.create(user=user, topic=topic, level=level)  # Use the authenticated user

        return validated_data

