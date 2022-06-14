from django.shortcuts import render

# Create your views here.
import json
import re

from django.http  import JsonResponse  
from django.views import View 

from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)

            username     = data['username']
            first_name   = data['first_name']
            last_name    = data['last_name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            USERNAME_VALIDATION     = '^([A-Za-z0-9가-힣]{2,})+'
            EMAIL_VALIDATION        = '^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$'
            PASSWORD_VALIDATION     = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{7,}$'
            PHONE_NUMBER_VALIDATION = '^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$'
            LAST_NAME_VALIDATION    = '^[a-zA-Z가-힣]+$'
            FIRST_NAME_VALIDATION   = '^[a-zA-Z가-힣]+$'

            if not re.match(USERNAME_VALIDATION,username):
                return JsonResponse({'message' : 'INVALID_USERNAME'}, status = 400)
            
            if not re.match(EMAIL_VALIDATION,email):
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)
            
            if not re.match(PASSWORD_VALIDATION,password):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400) 
            
            if not re.match(PHONE_NUMBER_VALIDATION,phone_number):
                return JsonResponse({'message' : 'INVALID_PHONE_NUMBER'}, status = 400)

            if not re.match(LAST_NAME_VALIDATION,last_name):
                return JsonResponse({'message' : 'INVALID_LAST_NAME'}, status = 400) 
            
            if not re.match(FIRST_NAME_VALIDATION,first_name):
                return JsonResponse({'message' : 'INVALID_LAST_NAME'}, status = 400) 

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'DUPLICATED_EMAIL'}, status=400) #서로 다른 사람이 같은 이메일 사용 불가

            User.objects.create(
                username     = username,
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                password     = password,
                phone_number = phone_number,
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)


class LogInView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)

            email_log_in    = data['email']
            password_log_in = data['password']

            if not User.objects.filter(email=email_log_in).exists():
                return JsonResponse({'message':'INVALED_USER'}, status=401)

            if not User.objects.filter(password=password_log_in).exists():
                return JsonResponse({'message':'INVALED_USER'}, status=401)

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
