import random

import profile
from tts import say

WORDS = {
    'who_are_you': {'groups': [['who', 'are', 'you']]},
    'how_am_i': {'groups': [['how', 'i', 'look'], ['how', 'am', 'i']]},
    'tell_joke': {'groups': [['tell', 'joke']]},
    'who_am_i': {'groups': [['who', 'am', 'i']]},
    'how_are_you': {'groups': [['how', 'are', 'you']]},
    'are_you_up': {'groups': [['you', 'up']]},
    'undefined': {'groups': []},
}


def who_are_you():
    va_name = profile.data['va_name']
    messages = ['I am ' + va_name + ', your lovely personal assistant.',
                va_name + ', didnt I tell you before?',
                'You ask that so many times! I am ' + va_name]
    say(random.choice(messages))


def how_am_i():
    replies = ['You are goddamn handsome!', 'My knees go weak when I see you.', 'You are sexy!',
               'You look like the kindest person that I have met.']
    say(random.choice(replies))


def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toad away.',
             'Why was six scared of seven? Because seven ate nine.',
             'What is the difference between snowmen and snowwomen? Snowballs.', 'No, I always forget the punch line.']
    say(random.choice(jokes))


def who_am_i():
    say('You are ' + profile.data['name'] + ', a brilliant person. I love you!')


def how_are_you():
    say('I am fine, thank you.')


def are_you_up():
    say('For you sir, always.')


def undefined():
    say('I dont know what that means!')
