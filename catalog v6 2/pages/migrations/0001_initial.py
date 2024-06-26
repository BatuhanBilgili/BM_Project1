# Generated by Django 5.0.1 on 2024-01-10 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('score', models.CharField(max_length=10)),
                ('match_date', models.DateTimeField()),
                ('isPublished', models.BooleanField(default=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='pages.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='pages.team')),
            ],
        ),
        migrations.CreateModel(
            name='LeagueTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_game', models.IntegerField(default=0)),
                ('win', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.team')),
            ],
        ),
    ]
