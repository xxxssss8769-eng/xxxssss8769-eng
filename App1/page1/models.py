from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=30)
    t = [('hypird','hypird'),('city','city'),('offroad','offroad'),('sport','sport'),('New','New'),('Hair','Hair')]
    type = models.CharField(max_length=20,choices=t)
    price = models.IntegerField()
    contact = models.TextField(max_length=500,blank=True)
    active = models.BooleanField(default=False)

                                                                # after end all migrate and makemigration
    def __str__(self):
        return self.name      #Products.objects = self.name
    class Meta:
        verbose_name='cars market'     #Products = market item
        ordering = ['name']       #sort abcd....



class Sign(models.Model):
    name = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name
