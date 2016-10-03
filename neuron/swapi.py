# -*- coding: utf-8 -*-

"""
neuron.swapi
~~~~~~~~~~~~

This module implements the Star Wars API.

:copyright: (c) 2012 by Franck Lebrun.
:license: Apache2, see LICENSE for more details.
"""

import requests

# import profile
# url = profile.data['swapi_url']

url = 'http://swapi.co/api/'


def get_param():
    """
    Get all the API Parameters.
    :return:
    """
    r = requests.get(url)
    print(r.json())


def get_result(request_type, request_id):
    """
    Function to get star wars API result.
    :param type: starships, people, vehicles, planets, films, species.
    :param id:
    :return:
    """
    if request_type:
        type_url = url + request_type
    if request_id:
        type_url = type_url + "/" + request_id

    r = requests.get(type_url)
    j = r.json()
    print(j)
    for key, value in j.items():
        if type(value) is list:
            print key + ": " + '[%s]' % '\n '.join(map(str, value))
        else:
            print(key + ": " + str(value))


# get_param()
#get_result('people', '')
get_result('people', '3')
#get_result('planets', '1')
