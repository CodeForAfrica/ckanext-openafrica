import datetime
from ckan.common import config

def current_year():
    year = datetime.datetime.now().year
    return year

def is_plugin_enabled(plugin_name):
    '''Returns a boolean True or False, indicating if the supplied plugin_name
    is enabled in the config file

    :param plugin_name: the name of the plugin to check for in the config file
    :type plugin_name: string
    '''
    config_plugins = config.get('ckan.plugins', '')
    config_plugins = ' ' + config_plugins + ' '
    plugin_name = ' ' + plugin_name + ' '
    if plugin_name in config_plugins:
        return True
    else:
        return False
