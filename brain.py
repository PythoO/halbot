import neuron.general_conversations
import neuron.profile as profile
from neuron.stt import stt
from neuron.tts import say

from neuron.general_conversations import WORDS as gc_words

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
        :param check:
        :return:
        """
        print(gc_words.keys())
        words_of_message = msg.split()
        print(words_of_message)
        for key in gc_words:
            for word in gc_words[key]['groups']:
                print word
                print words_of_message
                if set(word).issubset(set(words_of_message)):
                    print('find')


    check_message(msg)


while True:
    message = stt()
    if message == 'quit':
        say('Good bye ' + name + ', have a nice day.')
        exit()
    else:
        brain(message)
