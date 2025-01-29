from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def my_credentials(request):
    data = {
        'email': 'sulemfelsi@gmail.com',
        'current_datetime': datetime.now().isoformat(),
        'github_url': 'https://github.com/vasitha1/hng0_user_credentials_api.git'
    }
    return JsonResponse(data)
