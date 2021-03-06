from rest_framework.serializers import ModelSerializer 
from .models import NewsModel, Car, Image

class NewsSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class CarPreviewSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'code', 'main_image']


class CarCompleteSerializer(ModelSerializer):
    class Meta:
        model = Car 
        fields = '__all__'
    def get_photo_url(self, car):
        request = self.context.get('request')
        photo_url = car.photo.url
        return request.build_absolute_uri(photo_url)

class Carimages(ModelSerializer):
    model  = Image
    fields = ['image']
    def get_photo_url(self, car):
        request = self.context.get('request')
        photo_url = car.photo.url
        return request.build_absolute_uri(photo_url)


