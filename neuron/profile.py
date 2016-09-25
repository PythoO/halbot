#import yaml
import config
data = 0


def load_profile():
    """
    Function to load the VA configuration.
    :return:
    """
    print('loading profile')
    global data
    #conf = open('config.yml')
    #data = yaml.safe_load(conf)
    data = config.data


load_profile()
