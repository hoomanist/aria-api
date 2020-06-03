from django.contrib import admin
from .models import NewsModel, Car, Image 

admin.site.register(NewsModel)
admin.site.register(Image)
admin.site.register(Car)
