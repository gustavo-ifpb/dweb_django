from django.db import models

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'filme'
        verbose_name_plural = 'filmes'


class Character(models.Model):

    name = models.CharField(max_length=150)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='cast')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'personagem'
        verbose_name_plural = 'personagens'