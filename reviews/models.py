from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from movies.models import Movie

class Review(models.Model):

    rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.movie.name} ({self.user.first_name}) - {self.rate}'

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'