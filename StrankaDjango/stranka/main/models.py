from django.db import models

# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField()
    url = models.URLField(blank=True)

class Car(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tovarni_znacka = models.TextField()
    obchodni_oznaceni = models.TextField()
    druh_vozidla = models.TextField()
    objem_motoru = models.TextField()
    pocet_valcu = models.TextField()
    kombinovany_vykon = models.TextField()
    typ_paliva = models.TextField()
    prevodovka = models.TextField()
    typ_pohonu = models.TextField()
    cena_skladoveho_vozu = models.TextField()
    cena_uveru = models.TextField()
    images = models.ImageField(upload_to='main/image/')

    def __str__(self):
        return self.title + self.description