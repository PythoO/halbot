"""

"""
import forecastio
import profile
from tts import say

api_key = profile.data['forecastio']
lat = profile.data['lat']
lng = profile.data['lng']

WORDS = {
    'forecast_currently': {
        'groups': [['forecast', 'currently'], ['forecast', 'now'], ['forecasts', 'now'], ['weather', 'now'],
                   ['what', 'weather', 'is', 'it']]},
    'forecast_weekly': {'groups': [['forecast', 'week'], ['forecast', 'weekly']]},
}


def forecast_currently():
    """
    Get the current forecast.
    :return:
    """
    forecast = get_forecast()
    currently = forecast.currently()
    say(currently.summary)
    say(str(currently.temperature) + ' celsius.')


def forecast_weekly():
    """
    Get the week forecast.
    :return:
    """
    forecast = get_forecast()
    daily = forecast.daily()
    say(daily.summary)


def get_forecast():
    return forecastio.load_forecast(api_key, lat, lng)
