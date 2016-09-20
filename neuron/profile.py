import yaml

data = 0


def load_profile():
    """
    Function to load the VA configuration.
    :return:
    """
    print('loading profile')
    global data
    conf = open('config.yml')
    data = yaml.safe_load(conf)
    conf.close()


load_profile()
