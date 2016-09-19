import random

# Halbot
from halbot import config
from halbot.tts import say

def who_are_you(text):
  va_name = config.hal['va_name']
  messages = ['I am ' + va_name + ', your lovely personal assistant.',
      va_name + ', didnt I tell you before?',
      'You ask that so many times! I am ' + va_name]
  tts(random.choice(messages))
