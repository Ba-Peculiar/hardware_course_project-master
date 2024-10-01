from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Temperature
from .serializer import TemperatureSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Global variable to track the relay state
relay_state = False  # Initially, relay is OFF

# Dashboard view (HTML page rendering)
def dashboard(request):
    return render(request, 'myapp/dashboard.html')

# Relay control view: Handles relay state via POST and GET requests
@csrf_exempt
@require_http_methods(["POST", "GET"])
def relay_control_view(request):
    global relay_state

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            relay_state_input = data.get('relay_state')

            if relay_state_input is not None:
                if relay_state_input == "true":
                    relay_state = True
                    # Code to turn relay ON (actual hardware interaction can go here)
                    return JsonResponse({'message': 'Relay turned ON', 'relay_state': 'true'}, status=200)
                elif relay_state_input == "false":
                    relay_state = False
                    # Code to turn relay OFF (actual hardware interaction can go here)
                    return JsonResponse({'message': 'Relay turned OFF', 'relay_state': 'false'}, status=200)
                else:
                    return JsonResponse({'error': 'Invalid relay state'}, status=400)
            else:
                return JsonResponse({'error': 'No relay state provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'GET':
        return JsonResponse({'relay_state': 'true' if relay_state else 'false'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Separate view to get relay status
def get_relay_status(request):
    global relay_state
    return JsonResponse({'relay_state': relay_state})

# View to get the latest temperature and humidity readings
def get_readings(request):
    latest_reading = Temperature.objects.order_by('-timestamp').first()

    if latest_reading:
        data = {
            'temperature': latest_reading.temperature,
            'humidity': latest_reading.humidity,
        }
    else:
        # Return default values if no data is found
        data = {
            'temperature': 0.0,
            'humidity': 0.0,
        }
    
    return JsonResponse(data)

# Temperature Detail view to retrieve a specific temperature entry
class TemperatureDetailView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all().order_by('-timestamp')
    serializer_class = TemperatureSerializer

# Temperature List view to list all temperature readings
class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all().order_by('-timestamp')
    serializer_class = TemperatureSerializer

# Create new temperature reading (for adding data)
class TemperatureCreateAPIView(generics.CreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
