from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Actor(models.Model):

    GENDER = (
        (0, 'Masculino'),
        (1, 'Feminino'),
    )

    name = models.CharField(max_length=150)
    gender = models.IntegerField(choices=GENDER)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ator'
        verbose_name_plural = 'atores'


class Movie(models.Model):

    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    obs = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='movies')
    photo = models.ImageField(blank=True, null=True)
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(350, 355)], format='JPEG', options={'quality': 60})
    detail = ImageSpecField(source='photo', processors=[ResizeToFill(475, 300)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'filme'
        verbose_name_plural = 'filmes'


class Character(models.Model):

    name = models.CharField(max_length=150)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='cast')
    photo = models.ImageField(blank=True, null=True)
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(255, 255)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'personagem'
        verbose_name_plural = 'personagens'