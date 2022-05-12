"""View module for handling requests about ratings"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models.rating import Rating
from raterprojectapi.models.player import Player


class RatingView(ViewSet):
    """Raterproject rating view"""

    def create (self, request):
        """Handles POST operations
        
        Returns
            Response -- JSON serialized rating instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CreateRatingSerializer(serializers.ModelSerializer):
    """JSON serializer for ratings
    """

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'game')