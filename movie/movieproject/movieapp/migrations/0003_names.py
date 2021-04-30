# Generated by Django 3.2 on 2021-04-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('year', models.IntegerField(default=0)),
            ],
        ),
    ]
