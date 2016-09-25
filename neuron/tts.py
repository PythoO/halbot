import subprocess
import sys
import profile as profile


def say(message):
    """
    This function takes a message as an argument and converts it to
    speech depending on the OS.
    """
    print(message)
    if sys.platform == 'darwin':
        tts_engine = 'say'
        if profile.data['va_darwin_gender'] == 'female':
            language = '-vVicki'
            return subprocess.call([tts_engine, language, message])
        elif profile.data['va_darwin_gender'] == 'robot':
            language = '-v' + profile.data['va_robot']
            return subprocess.call([tts_engine, language, message])
        else:
            return subprocess.call([tts_engine, message])

    elif sys.platform.startswith('linux') or sys.platform == 'win32':
        tts_engine = 'espeak'
        if profile.data['va_gender'] == 'female':
            language = '-ven+f3'
            speed = '-s170'
            return subprocess.call([tts_engine, language, speed, message])
        else:
            speed = '-s170'
            return subprocess.call([tts_engine, speed, message])
