import sys
import subprocess

import config

def say(message):
  """
  This function takes a message as an argument and converts it to
  speech depending on the OS.
  """
  if sys.platform == 'darwin':
      tts_engine = 'say'
      if config.hal['va_gender'] == 'male':
        language = '-valex'
        return subprocess.call([tts_engine, language, message])
      else:
        return subprocess.call([tts_engine, message])
  elif sys.platform.startswith('linux') or sys.platform == 'win32':
      tts_engine = 'espeak'
      if config.hal['va_gender'] == 'female':
        language = '-ven+f3'
        speed= '-s170'
        return subprocess.call([tts_engine, language, speed, message])
      else:
        speed= '-s170'
        return subprocess.call([tts_engine, speed, message])
