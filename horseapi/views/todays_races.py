# horseapi/views/todays_races.py
import requests
from django.http import JsonResponse
from django.conf import settings
from requests.auth import HTTPBasicAuth

def get_todays_races(request):
    api_username = settings.RACING_API_USERNAME
    api_password = settings.RACING_API_PASSWORD
    base_url = 'https://api.theracingapi.com/v1/racecards/free'

    # Get query parameters from request
    day = request.GET.get('day', 'today')
    region_codes = request.GET.get('region_codes')

    params = {'day': day}
    if region_codes:
        params['region_codes'] = region_codes

    response = requests.get(base_url, params=params, auth=HTTPBasicAuth(api_username, api_password))
    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch race data'}, status=response.status_code)
