from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Car, NewsModel, Image
from .serializers import CarPreviewSerializer, CarCompleteSerializer, NewsSerializer, Carimages
from rest_framework.response import Response
from rest_framework.decorators import api_view

def carpreview(request):
    if request.method == "GET":
        query = Car.objects.all()
        serialize = CarPreviewSerializer(query, many=True)
        return JsonResponse(serialize.data, safe=False)

def news(request):
    if request.method == "GET":
        query = NewsModel.objects.all()
        serialize = NewsSerializer(query, context={"request": request}, many=True)
        return JsonResponse(serialize.data, safe=False)


@api_view(('GET', ))
def carcomplete(request):
    if request.method == "GET":
        query = Car.objects.get(code=int(request.GET["code"]))
        serialize = CarCompleteSerializer(query)
        return Response(serialize.data)

@api_view(('GET', ))
def images(request):
    if request.method == "GET":
        car_query = Car.objects.get(code=int(request.GET["code"]))
        images_query = Image.objects.filter(car=car_query) 
        serialize = Carimages(images_query, many=True)
        return Response(serialize.data)




