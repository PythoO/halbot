import requests

WORDS = {
    'get_pipo': {'groups': [['pipotron'], ['pipo']]},
}


def get_pipo():
    r = requests.get('http://www.pipotron.free.fr/')
    print(r.text)
