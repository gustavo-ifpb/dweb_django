from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)


class MovieAdmin(admin.ModelAdmin):

    list_display = ('name', )
    filter_horizontal = ('category',)


class ActorAdmin(admin.ModelAdmin):

    list_display = ('name', 'gender')


class CharacterAdmin(admin.ModelAdmin):

    list_display = ('name', 'movie', 'actor')

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Actor, ActorAdmin)
admin.site.register(models.Character, CharacterAdmin)