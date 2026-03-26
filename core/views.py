from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactMessage
import os

def home(request):
    return render(request, 'base.html', {
        'google_maps_key': os.environ.get('GOOGLE_MAPS_API_KEY')
    })

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Save message impressively
            ContactMessage.objects.create(
                name=data.get('name', '').strip(),
                email=data.get('email', '').strip(),
                phone=data.get('phone', '').strip(),
                message=data.get('message', '').strip()
            )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you! Your message has been received successfully.'
            })
            
        except Exception:
            return JsonResponse({
                'status': 'error',
                'message': 'Oops! Something went wrong. Please try again.'
            }, status=400)
    
    return JsonResponse({'status': 'error'}, status=405)