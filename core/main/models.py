from django.db import models

# Create your models here.
class Cattleya(models.Model):
    name = models.CharField('Cattleya name', max_length=30)
    about = models.TextField('Cattleya about')
    img = models.ImageField('cattleya image', upload_to='media')
class Dendrobium(models.Model):
    name = models.CharField('Dendrobium name', max_length=30)
    about = models.TextField('Dendrobium about')
    img = models.ImageField('Dendrobium image', upload_to='media')
class Chiloschista(models.Model):
    name = models.CharField('Chiloschista name', max_length=30)
    about = models.TextField('Chiloschista about')
    img = models.ImageField('Chiloschista image', upload_to='media')
class Vanda(models.Model):
    name = models.CharField('Vanda name', max_length=30)
    about = models.TextField('Vanda about')
    img = models.ImageField('Vanda image', upload_to='media')


    def __str__(self):
        return self.name

