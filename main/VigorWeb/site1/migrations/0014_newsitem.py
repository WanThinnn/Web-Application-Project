# Generated by Django 5.0.6 on 2024-05-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0013_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField(unique=True)),
                ('description_text', models.TextField()),
                ('image', models.URLField()),
            ],
        ),
    ]