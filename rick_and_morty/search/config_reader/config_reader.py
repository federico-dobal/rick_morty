import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../', 'config', 'config.properties'))


def getRickAndMortyApiUrl():
    """
        Get the API URL to access GraphQL API from configuration file
    """
    return config.get('ApiSection', 'rick.morty.api.url');
