# Generated by Django 3.1.3 on 2020-11-05 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_obs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'ator',
                'verbose_name_plural': 'atores',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'filme', 'verbose_name_plural': 'filmes'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cast', to='movies.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.movie')),
            ],
            options={
                'verbose_name': 'personagem',
                'verbose_name_plural': 'personagens',
            },
        ),
    ]