from django.shortcuts import render

# Create your views here.
import json
import re
from django.forms import PasswordInput
from django.http import JsonResponse
from django.views import View
from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError
from users.models import *



class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])
            if not ValidationError :
                return JsonResponse({"message": "ERROR_EMAIL_VALIDATION"}, status=400)
            # validation 에러를 사용해보고 싶어서 이메일은 정규식 대신 사용해봤습니다

            if (data["email"] == "") or (data["password"] == ""):
                return JsonResponse({"message": "ERROR_EMPTY_EMAIL_OR_PASSWORD"}, status=400)
            # 데이터가 안들어올경우

            if User.objects.filter(email=data["email"]).exists() :
                return JsonResponse({"message": "ERROR_EMAIL_ALREADY_EXIST"}, status=400)
            # 중복된 이메일

            if re.match(
                r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$', 
                'password'):
                return JsonResponse({"message": "ERROR_REQUIRE_8_LETTER,NUMBER,SPECIAL_SYMBOLS)"}, status=400)
            # 패스워드 검사 정규식

            User.objects.create(
                first_name   = data['first_name'],
                last_name    = data['last_name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],

        )
            
            return JsonResponse({"message": "SUCCESS"}, status=201)
            
        except KeyError:
                return JsonResponse({"message": "KEY_ERROR"}, status=400)