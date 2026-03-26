from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactMessage

def home(request):
    return render(request, 'base.html', {
        'google_maps_key': os.environ.get('GOOGLE_MAPS_API_KEY')
    })

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Save message to database
            ContactMessage.objects.create(
                name=data.get('name', ''),
                email=data.get('email', ''),
                phone=data.get('phone', ''),
                message=data.get('message', '')
            )
            
            return JsonResponse({
                'status': 'success', 
                'message': 'Thank you! Your message has been received.'
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Something went wrong.'}, status=400)
    
    return JsonResponse({'status': 'error'}, status=405)