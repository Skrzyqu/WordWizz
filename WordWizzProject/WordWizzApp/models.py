from django.db import models

# Create your models here.
from django.db import models

class Word(models.Model):
    polish_word = models.TextField()
    german_word = models.TextField()

    def __str__(self):
        return f"{self.polish_word} - {self.german_word}"