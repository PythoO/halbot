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
    return_msg = random.choice(messages)
    say(return_msg)


def how_am_i():
    replies = ['You are goddamn handsome!', 'My knees go weak when I see you.', 'You are sexy!',
               'You look like the kindest person that I have met.']
    return_msg = random.choice(replies)
    say(return_msg)


def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toad away.',
             'Why was six scared of seven? Because seven ate nine.',
             'What is the difference between snowmen and snowwomen? Snowballs.', 'No, I always forget the punch line.']
    return_msg = random.choice(jokes)
    say(return_msg)


def who_am_i():
    name = profile.data['name']
    me = ['You are ' + name + ', a brilliant person. I love you!',
          'I know that question, you are ' + name,
          ]
    return_msg = random.choice(me)
    say(return_msg)


def how_are_you():
    me = ['I am fine, thank you.',
          'I\'m not bad, thank you',
          ]
    return_msg = random.choice(me)
    say(return_msg)


def are_you_up():
    say('For you sir, always.')


def undefined():
    say('I dont know what that means!')
