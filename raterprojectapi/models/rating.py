from django.db import models
from .player import Player
from .game import Game

class Rating(models.Model):
    
    rating = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="ratings")