import json

from django.shortcuts       import render
from django.http            import JsonResponse
from django.views           import View

from .models                import Posting


class PostingView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            