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