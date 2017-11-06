from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        return HttpResponseRedirect('/' + latitude + '&' + longitude + '/')
    return render(request, 'home.html')


def result(request):
    import pyowm
    import json

    API_KEY = '3d687c8dd758a1e889ae152a71968950'

    """Getting coordinates from url path"""
    path = request.path.split('&')
    latitude = float(path[0][1:])
    longitude = float(path[1][:-1])

    """Getting temperature data for Geolocation"""
    owm = pyowm.OWM(API_KEY)
    observation = owm.weather_at_coords(latitude, longitude)
    w = observation.get_weather()
    """Getting name of the station for Geolocation"""
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

    return render(request, 'result.html', {'request': request, 'location_name': location_name, 'avg_temp': avg_temp,
                                           'latitude': latitude, 'longitude': longitude})