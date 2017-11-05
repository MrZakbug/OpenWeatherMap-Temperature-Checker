from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.forms import NumberInput


def home(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        # if latitude.is_valid() and longitude.is_valid():
        return HttpResponseRedirect('/' + latitude + '&' + longitude + '/')
    # else:
    #     return HttpResponseRedirect('/error/')
    return render(request, 'home.html')


def result(request):
    import pyowm
    import json

    API_KEY = '3d687c8dd758a1e889ae152a71968950'

    owm = pyowm.OWM(API_KEY)
    observation = owm.weather_at_coords(-34.123, 80.0)
    w = observation.get_weather()
    raw = observation.to_JSON()
    processed = json.loads(raw)
    try:
        location_name = processed['Location']['country'] + '-' + processed['Location']['name']
    except TypeError:
        if processed['Location']['name'] != '':
            location_name = processed['Location']['name']
        elif processed['Location']['country'] is not None:
            location_name = processed['Location']['country']
        else:
            location_name = 'Not found'
    avg_temp = w.get_temperature('celsius')['temp']

    return render(request, 'result.html', {'location_name': location_name, 'avg_temp': avg_temp})