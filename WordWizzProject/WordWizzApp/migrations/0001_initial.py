# Generated by Django 5.1.4 on 2024-12-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polish_word', models.TextField()),
                ('german_word', models.TextField()),
            ],
        ),
    ]
