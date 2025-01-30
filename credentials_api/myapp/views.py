from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def my_credentials(request):

    current_datetime_utc = datetime.now(timezone.utc)
    current_datetime_iso = current_datetime_utc.isoformat().replace('+00:00', 'Z')

    data = {
        'email': 'sulemfelsi@gmail.com',
        'current_datetime': current_datetime_iso,
        'github_url': 'https://github.com/vasitha1/hng0_user_credentials_api'
    }
    return JsonResponse(data)
