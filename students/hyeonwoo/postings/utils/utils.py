import jwt
import json

from users.models       import User
from westagram.settings import SECRET_KEY, ALGORITHM
from django.http        import JsonResponse

# class LoginConfirm:
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, request, *args, **kwargs):

#         if "Authorization" not in request.headers:
#             return JsonResponse({"message" : "INVALID_LOGIN"}, status=401)

#         token = request.headers.get("Authorization", None)

#         try:
#             if token:
#                 token_payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
#                 user          = User.objects.get(id=token_payload['user_id'])
#                 request.user = user
#                 return self.original_function(self, request, *args, **kwargs)

#             return JsonResponse({'message' : "NEED_LOGIN"}, status=401)

#         except jwt.DecodeError:
#             return JsonResponse({'message' : 'INVALID_USER'}, status=401)

#         except User.DoesNotExist:
#             return JsonResponse({'message' : 'INVALID_USER'}, status=401)  
# 

def login_decorator(func):

    def wrapper(self, request, *args, **kwargs):

        if "Authorization" not in request.headers:
            return JsonResponse({"message" : "INVALID_LOGIN"}, status=401)

        token = request.headers.get("Authorization", None)

        try:
            if token:
                token_payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
                user          = User.objects.get(id=token_payload['user_id'])
                request.user = user

                return func(self, request, *args, **kwargs)

            return JsonResponse({'message' : "NEED_LOGIN"}, status=401)

        except jwt.DecodeError:
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)          