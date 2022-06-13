import json
from django.core.exceptions import ValidationError

from django.shortcuts   import render
from django.http        import JsonResponse
from django.views       import View

from .validation        import validation_email, validation_password
from .models            import User

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        try :
            first_name    = data['first_name']
            last_name     = data['last_name']
            user_name     = data['user_name']
            email         = data['email']
            password      = data['password']
            mobile_number = data['mobile_number']

            validation_email(email)
            validation_password(password)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE' : 'ALREADY_EXISTS_EMAIL'}, status=400)

            User.objects.create(
                first_name    = first_name,
                last_name     = last_name,
                user_name     = user_name,
                email         = email,
                password      = password,
                mobile_number = mobile_number
            )

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 201)
        
        except KeyError :
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

        except ValidationError as e:
            return JsonResponse({"MESSAGE" : (e.message)}, status = 400)


    # def get(self, request):
    #     users = User.objects.all()
    #     results = []

    #     for user in users:
    #         results.append(
    #             {
    #                 "first_name"    : user.first_name,
    #                 "last_name"     : user.last_name,
    #                 "user_name"     : user.user_name,
    #                 "email"         : user.email,
    #                 "password"      : user.password,
    #                 "mobile_number" : user.mobile_number
    #             }
    #         )
        
    #     return JsonResponse({"results" : results}, status=200)

    

