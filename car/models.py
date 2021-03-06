from django.db import models
from django.utils.timezone import now

class Car(models.Model):
    main_image = models.ImageField( null=True, blank=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    EngineVolume = models.IntegerField()      
    mileage = models.BigIntegerField()
    Price = models.BigIntegerField()
    code = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"{self.brand} {self.name} {self.year}"
class NewsModel(models.Model):
    date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, to_field='code')
    image = models.ImageField()
