from django.db import models


class Game(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    year_released = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.CharField(max_length=50)
    age_recommendation = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    organizer = models.ForeignKey("Player", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", related_name="games")
    
    @property
    def editable(self):
        return self.__editable
    
    @editable.setter
    def editable(self, value):
        self.__editable = value 
        
    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating
        
        # Calculate the averge and return it.
        # If you don't know how to calculate averge, Google it.
        average_rating = total_rating / ratings * 100
        #return the result
        return average_rating