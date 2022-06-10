# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from users.models import *



class JoinView(View):
    #제대로된 값이 안들어올 경우 400 오류 리턴
    #이메일이 이상하면 에러 리턴
    #패스워드 오류시 리턴 
    # 이메일 중복 확인
    def post(self, request):
        data = json.loads(request.body)

        user = User.objects.create(
            name = data['name']
            email = data['email']
        )

