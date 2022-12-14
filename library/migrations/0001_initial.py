# Generated by Django 4.0.4 on 2022-09-27 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('written', models.DecimalField(decimal_places=0, max_digits=4)),
                ('genre', models.CharField(choices=[('Horror', 'Horror'), ('Romance', 'Romance'), ('Sci-fi', 'Sci-fi'), ('Adventure', 'Adventure'), ('None-fiction', 'None-fiction'), ('Drama', 'Drama'), ('History', 'History'), ('Science', 'Science'), ('Technology', 'Technology'), ('Art', 'Art'), ('Autobiography', 'Autobiography'), ('Other', 'Other')], max_length=25)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('not available', 'Not available')], max_length=20)),
                ('description', models.TextField(null=True)),
                ('slug', models.SlugField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
    ]
