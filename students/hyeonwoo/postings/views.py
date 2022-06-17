import json
import re

from django.shortcuts       import render
from django.http            import JsonResponse
from django.views           import View

from .models                import Posting
from users.models           import User
from .utils.utils           import login_decorator


class PostingView(View):
    @login_decorator
    def post(self, request):
        try:
            data      = json.loads(request.body)
            user      = request.user
            image_url = data["image_url"] #data.get('imgae_url', None)
            postname  = data["postname"]
            contents  = data["contents"]

            Posting.objects.create(
                user       = user,
                image_url  = image_url,
                postname   = postname,
                contents   = contents
            )

            return JsonResponse({"MESSAGE" : "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

    @login_decorator
    def get(self, request):
        try:
            user    = request.user
            results = []
            results.append(
                {
                    "1. user_name"        : user.user_name,
                    "2. postname"         : user.postings.get(user_id=user.id).postname,
                    "3. image_url"        : user.postings.get(user_id=user.id).image_url,
                    "4. contents"         : user.postings.get(user_id=user.id).contents,        
                    "5. created_at"       : user.postings.get(user_id=user.id).created_at
                }
            )
            return JsonResponse({"results" : results}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE' : "KEY_ERROR"}, status=400)
            
            

        


