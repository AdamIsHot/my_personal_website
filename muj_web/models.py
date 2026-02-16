from django.db import models

# Create your models here.

from django.db import models

class Clanek(models.Model):
    titulek = models.CharField(max_length=200)
    obsah = models.TextField()
    datum_vydani = models.DateTimeField(auto_now_add=True)
    nahledovy_obrazek = models.ImageField(upload_to='clanky/obrazky/', blank=True, null=True)

    def __str__(self):
        return self.titulek