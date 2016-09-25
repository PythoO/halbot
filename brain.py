import neuron.general_conversations
import neuron.profile as profile
from neuron.stt import stt
from neuron.tts import say

from neuron.general_conversations import WORDS as gc_words
from neuron.forecast import WORDS as fc_words

name = profile.data['name']
say('Welcome ' + name + ', systems are now ready to run. How can I help you?')


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
        if not find:
            neuron.general_conversations.undefined()

    check_message(msg)


while True:
    message = stt()
    if message == 'quit':
        say('Good bye ' + name + ', have a nice day.')
        exit()
    else:
        brain(message)
