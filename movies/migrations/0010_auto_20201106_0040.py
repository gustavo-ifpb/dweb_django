# Generated by Django 3.1.3 on 2020-11-06 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20201106_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.actor'),
        ),
    ]