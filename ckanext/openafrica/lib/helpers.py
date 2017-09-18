# encoding: utf-8

# Copyright (c) 2015-2017 Code for Africa

# This file is part of CKAN openAFRICA Extension.

# CKAN openAFRICA Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# CKAN openAFRICA Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN openAfrica Extension. If not, see <http://www.gnu.org/licenses/>.

u'''Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
It is an extension of ckan helpers.py
'''
import datetime
from ckan.common import config

def current_year():
    u'''Return the current year'''
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
