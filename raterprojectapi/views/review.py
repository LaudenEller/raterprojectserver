"""View module for handling requests about reviews"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models.review import Review
from raterprojectapi.models.player import Player

class reviewView(ViewSet):
    """Level up review view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single review 
        
        Returns:
            Response -- JSON serialized review
        """
        
        try:
            review = Review.objects.get(pk=pk)
            serializer = reviewSerializer(review)
            return Response(serializer.data)
        except review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET requests to get all reviews
        
        Returns:
            Response -- JSON serialized list of review types
        """
        
        # reviews = review.objects.annotate(event_count=Count('events'))
        reviews = Review.objects.all()
        # review_type = request.query_params.get('type', None)
        # if review_type is not None:
        #     reviews = reviews.filter(review_type_id=review_type)
            
        serializer = reviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized review instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreatereviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CreatereviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """

    class Meta:
        model = Review
        fields = ('id', 'review', 'game')

class reviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """
    
    # event_count = serializers.IntegerField(default=None)
    
    class Meta:
        model = Review
        depth = 2 # INSQ: This will embed all the data the client is 
                            # looking for so that the relevant objects themselves are returned instead of just the FK ids
        fields = ('id', 'review', 'player', 'game')