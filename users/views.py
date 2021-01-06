from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth.models import User
from django.contrib.auth import *
from .serializers import UsersAllSerializer
# Create your views here.


    
@csrf_exempt
def users(request):
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UsersAllSerializer(query_set,many=True)

        return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def id_overlap(request):         #{"user_id":""} /id중복검사 

    if request.method == 'POST':
        # id= request.POST.get('user_id','')
        id = JSONParser().parse(request)['user_id']
        print('DEBUG','id=',id)
        if User.objects.filter(username=id).exists():
            return JsonResponse({'code':'1001','massage':'아이디 중복'},status=200)
        
        return JsonResponse({'code':'0000','massage':'중복 없음'},status=200)




@csrf_exempt
def signup(request):        #{"user_id":"","user_password1":"",,"user_password2":""} 0000:성공 1001:실패

    if request.method == 'POST':
        # id=request.POST.get('user_id','')
        # password1=request.POST.get('user_password1','')
        # password2=request.POST.get('user_password2','')
        data=JSONParser().parse(request)
        id=data['user_id']
        password1=data['user_password1']
        password2=data['user_password2']
        print('DEBUG','id=',id,'pw1=',password1,'pw2=',password2)
        if password1==password2:
            User.objects.create_user(username=id,password=password1)

            return JsonResponse({'code':'0000','msg':'가입 성공'},status=200)

        return JsonResponse({'code':'1001','msg':'비밀번호 확인'},status=200)

@csrf_exempt
def login(request):     #{"user_id":"","user_password":""} 0000:성공 1001:실패
    if request.method == 'POST':
        # id=request.POST.get('user_id','')
        # password=request.POST.get('user_password','')
        data=JSONParser().parse(request)
        id=data['user_id']
        password=data['user_password']
        result=authenticate(username=id,password=password)
        if result:
            return JsonResponse({'code':'0000','msg':'로그인 성공'},status=200)

        else:
            return JsonResponse({'code':'1001','msg':'로그인 실패'},status=200)

        


# @csrf_exempt
# def email_overlap(request):         #{"user_email":""} /email중복검사 202:allow 400:overlap

#     if request.method == 'POST':
#         data = JSONParser().parse(request)

#         try:
#             Users.objects.get(user_email=data['user_email'])
#         except:
#             return HttpResponse(status=202)
#         return HttpResponse(status=400)
