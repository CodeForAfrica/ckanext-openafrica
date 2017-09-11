import datetime
from ckan.common import config

def current_year():
    year = datetime.datetime.now().year
    return year

def enable_datarequest():
    config_plugins = config.get('ckan.plugins', None)
    if ' datarequests ' in config_plugins:
        return True
    else:
        return False

