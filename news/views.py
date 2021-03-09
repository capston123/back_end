from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from news.models import News

# Create your views here.
@csrf_exempt
def news(request):
    if request.method == 'POST':
        date = JSONParser().parse(request)['date']
        query_set = News.objects.filter(date=date)
        serializer = NewsSerializer(query_set,many=True)

        return JsonResponse(serializer.data,safe=False)