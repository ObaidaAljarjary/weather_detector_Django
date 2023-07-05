from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(
            'https://api.weatherapi.com/v1/current.json?key=45d85cd349f243d6a7d160104231706&q='+city+'&aqi=yes').read()
        json_data = json.loads(res)
        print(json_data)
        data = {
            "country": str(json_data['location']['country']),
            "temp": str(json_data['current']['temp_c']) + 'c',
            "humidity": str(json_data['current']['humidity']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
