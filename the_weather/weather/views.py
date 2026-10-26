from django.shortcuts import render, redirect, get_object_or_404
import os
import requests
from .models import City
from .forms import CityForm

def delete_city(request, city_id):
    if request.method == 'POST':
        city = get_object_or_404(City, id=city_id)
        city.delete()
    return redirect('/')

def index(request):

    api_key = os.environ.get('OPENWEATHER_API_KEY', '')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={{}}&units=imperial&appid={api_key}'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = CityForm()
    cities = City.objects.all()

    weather_data = []

    for city in cities: 

        city_weather = requests.get(url.format(city)).json()

        if 'main' not in city_weather:
            continue

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)