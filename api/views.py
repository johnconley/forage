import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db import models
from django.http import HttpResponse

def locate(request):
    # Turn the request into a lat and long
    # Fetch all restaurants from the database
    # Go through all of the restaurants and find the closest ones
    # Return those as JSON

    lat = float(reqest.GET['lat'])
    lng = float(request.GET['long'])
    restaurants = get_restaurants(lat, lng)

    response_data = {}
    dlist = []
    for r in restaurants:
        r_dic = {}
        r["name"] = restaurant.name
        r["genre"] = restaurant.genre
        r["latitude"] = restaurant.latitude
        r["longitude"] = restaurant.longitude
        r["address"] = restaurant.address
        dlist.append(r_dic)

    return HttpResponse(json.dumps(response_data), content_type="application/json")

# returns the ten closest restaurants to (latitude, longitude)
def get_restaurants(restaurants, latitude, longitude):
    restaurants = Restaurant.objects.all()

    def calculate_distance(restaurant):
        rst_lat = restaurant.latitude
        rst_long = restaurant.longitude
        math.hypot(latitude - rst_lat, longitude - rst_long) # pythagorean theorem
        return [distance, restaurant]

    restaurantsWithDistance = map(calculate_distance, restaurants)
    restaurantsWithDistance = sorted(restaurantsWithDistance, key = lambda x : x[0])
    return restaurantsWithDistance[:10]
