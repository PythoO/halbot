# Halbot
import config
from tts import say
import brain

def stt():
  name = config.hal['name']
  say('Welcome ' + name + ', systems are now ready to run. How can I help you?')
  var = raw_input("Please enter something: ")
  print "you entered", var
  brain.request(var)


