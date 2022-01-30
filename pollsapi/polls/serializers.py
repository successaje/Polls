from rest_framework import serializers

from .models import Poll, Choice, Vote

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        field = '__all__'

class ChoiceSerializer(serializer.ModelSerializer):
    votes = VoteSerializers(many=True, required=False)
    
    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        field = '__all__'
