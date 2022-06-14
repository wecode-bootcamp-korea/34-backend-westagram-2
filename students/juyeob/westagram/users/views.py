
import json
import re

from django.http  import JsonResponse
from json.decoder import JSONDecodeError
from django.views import View

from users.models import User

class SignUpView(View):
    def post(self, request):

        try:
            data = json.loads(request.body)

            first_name   = data['first_name']
            last_name    = data['last_name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            if not re.match(
                '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                return JsonResponse({"message": "ERROR_EMAIL_VALIDATION"}, status=400)

            if not re.match(
                '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$', password):
                return JsonResponse({"message": "ERROR_REQUIRE_8_LETTER,NUMBER,SPECIAL_SYMBOLS)"}, status=400)

            if User.objects.filter(email = email).exists() :
                return JsonResponse({"message": "ERROR_EMAIL_ALREADY_EXIST"}, status=400)

            User.objects.create(
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                password     = password,
                phone_number = phone_number,

            )
            
            return JsonResponse({"message": "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)