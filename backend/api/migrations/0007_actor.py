# Generated by Django 4.0.10 on 2023-02-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_movie_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('movies', models.ManyToManyField(to='api.movie')),
            ],
        ),
    ]
