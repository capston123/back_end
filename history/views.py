from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from .serializers import *
from history.models import History
# Create your views here.
    
@csrf_exempt
# Create your views here.
def hisotry(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        user_id = data['user_id']
        category = data['content_type'] + '-' + data['content_category']
        content_number = data['content_number']

        if History.objects.filter(user_id=user_id).exists():
            
            History.objects.create(user_id=user_id, category=category, content_number=content_number)        
            return JsonResponse({'code' : '0000', 'msg' : '데이터 전송 성공'}, status=200)
        
        return JsonResponse({'code' : '1001', 'msg' : '데이터 전송 실패'}, status=200)