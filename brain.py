import speech_recognition as sr
import neuron
import neuron.profile as profile
from neuron.stt import stt
from neuron.tts import say

from neuron.general_conversations import WORDS as gc_words
from neuron.forecast import WORDS as fc_words
from neuron.twitter import WORDS as twitter_words
from neuron.pipotron import WORDS as pipo_words

name = profile.data['name']
IBM_user = profile.data['IBM_user']
IBM_pass = profile.data['IBM_pass']


# say('Welcome ' + name + ', systems are now ready to run. How can I help you?')


def brain(msg):
    """
    This is the brain, it's work like a controller.
    :param msg:
    :return:
    """

    def check_message(msg):
        """
        Check wich neuron to use.
        :param msg:
        :return:
        """
        words_of_message = msg.split()
        find = False
        for key in gc_words:
            if words_of_message in gc_words[key]['groups']:
                getattr(neuron.general_conversations, key)()
                find = True
                break
        for key in fc_words:
            if words_of_message in fc_words[key]['groups']:
                getattr(neuron.forecast, key)()
                find = True
                break
        for key in twitter_words:
            if words_of_message in twitter_words[key]['groups']:
                getattr(neuron.twitter, key)()
                find = True
                break
        for key in pipo_words:
            if words_of_message in pipo_words[key]['groups']:
                getattr(neuron.pipotron, key)()
                find = True
                break
        if not find:
            neuron.general_conversations.undefined()

    check_message(msg)


while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something !!')
        audio = r.listen(source)

    try:
        speech_msg = r.recognize_ibm(audio, username=IBM_user, password=IBM_pass).lower()

        print("IBM Speech think you say : " + speech_msg)
    except sr.UnknownValueError:
        print('IBM Speech could not understand audio')
    except sr.RequestError as e:
        print("Could not request result from IBM; {0}".format(e))

    if speech_msg == 'quit':
        say('Good bye ' + name + ', have a nice day.')
        exit()
    else:
        brain(speech_msg)
