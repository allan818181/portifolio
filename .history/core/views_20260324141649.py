from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'base.html', {
        'google_maps_key': os.environ.get('GOOGLE_MAPS_API_KEY')
    })

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success', 'message': 'Thank you! Your message has been received.'})
    return JsonResponse({'status': 'error'}, status=405)