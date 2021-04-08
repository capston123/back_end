from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from .serializers import *
from history.models import History
from youtube.models import Youtube
from webtoons.models import Naver,Daum
from news.models import News
from youtube import serializers as ys
from news import serializers as ns
from webtoons import serializers as ws
# Create your views here.

@csrf_exempt
def hisotry(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        user_id = data['user_id']
        category = data['category'] 
        content_number = data['content_number']
        content_class = data['content_class']
        
        obj=History(user_id=user_id, category=category, content_number=content_number,content_class=content_class)

        if not History.objects.filter(user_id=user_id,content_number=content_number,category=category,content_class=content_class).exists():
            obj.save()

            return JsonResponse({'code' : '0000', 'msg' : '데이터 전송 성공'}, status=200)
        else:
            return JsonResponse({'code' : '0001', 'msg' : '데이터 중복'}, status=200)



@csrf_exempt
def recomend_youtube(request):
    if request.method =='POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='youtube')
        contents_scores={}
        for u_h in user_history:
            categorys= list(u_h.category.split(','))
            for ca in categorys:
                if ca in contents_scores:
                    contents_scores[ca]+=1
                else:
                    contents_scores[ca]=1
        result=sorted(contents_scores.items(),key=lambda x:x[1])
        obj=Youtube.objects.filter(category__icontains=result[0][0])
        serializer = ys.YoutubeSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def recomend_naver(request):
    if request.method =='POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='naver_toon')
        contents_scores={}
        for u_h in user_history:
            categorys= list(u_h.category.split(','))
            for ca in categorys:
                if ca in contents_scores:
                    contents_scores[ca]+=1
                else:
                    contents_scores[ca]=1
        result=sorted(contents_scores.items(),key=lambda x:x[1])
        obj=Naver.objects.filter(category__icontains=result[0][0])
        serializer = ws.NaverSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def recomend_daum(request):
    if request.method =='POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='daum_toon')
        contents_scores={}
        for u_h in user_history:
            categorys= list(u_h.category.split(','))
            for ca in categorys:
                if ca in contents_scores:
                    contents_scores[ca]+=1
                else:
                    contents_scores[ca]=1
        result=sorted(contents_scores.items(),key=lambda x:x[1])
        obj=Daum.objects.filter(category__icontains=result[0][0])
        serializer = ws.DaumSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def recomend_news(request):
    if request.method =='POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='news')
        contents_scores={}
        for u_h in user_history:
            categorys= list(u_h.category.split(','))
            for ca in categorys:
                if ca in contents_scores:
                    contents_scores[ca]+=1
                else:
                    contents_scores[ca]=1
        result=sorted(contents_scores.items(),key=lambda x:x[1])
        obj=News.objects.filter(category__icontains=result[0][0])
        serializer = ns.NewsSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def history_news(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='news')
        content_id = []
        for u_h in user_history:
            content_id.append(u_h.content_number)
        obj=News.objects.filter(id__in=content_id)
        serializer = ns.NewsSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def history_youtube(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='youtube')
        content_id = []
        for u_h in user_history:
            content_id.append(str(u_h.content_number))
        obj=Youtube.objects.filter(id__in=content_id)
        serializer = ys.YoutubeSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def history_naver(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='naver_toon')
        content_id = []
        for u_h in user_history:
            content_id.append(str(u_h.content_number))
        print(content_id)
        obj=Naver.objects.filter(id__in=content_id)
        print(obj)
        serializer = ws.NaverSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def history_daum(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        user_id =data['user_id']
        user_history=History.objects.filter(user_id=user_id,content_class='daum_toon')
        content_id = []
        for u_h in user_history:
            content_id.append(u_h.content_number)
        obj=Daum.objects.filter(id__in=content_id)
        serializer = ws.DaumSerializer(obj,many=True)

        return JsonResponse(serializer.data,safe=False)