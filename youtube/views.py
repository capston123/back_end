from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from youtube.models import Youtube
# Create your views here.
    
@csrf_exempt
def youtube(request):
    if request.method == 'POST':
        date = JSONParser().parse(request)['date']
        query_set = Youtube.objects.filter(date__istartswith=date)
        serializer = YoutubeSerializer(query_set,many=True)

        return JsonResponse(serializer.data,safe=False)

# Create your views here.
