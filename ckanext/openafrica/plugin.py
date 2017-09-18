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
# along with CKAN openAFRICA Extension. If not, see <http://www.gnu.org/licenses/>.

u'''Defines OpenAfrica plugin
Extends CKAN plugins core which provides plugin services to the CKAN
'''

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class OpenAfricaPlugin(plugins.SingletonPlugin):
    u'''OpenAfrica templating plugin done in 2015.

    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        u'''
        Called by load_environment at earliest point when config is
        available to plugins. The config should be updated in place.

        :param config: ``config`` object
        '''
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'openafrica')

    def before_map(self, map):
        u'''
        Called before the routes map is generated. ``before_map`` is before any
        other mappings are created so can override all other mappings.

        :param map: Routes map object
        :returns: Modified version of the map object
        '''
        map.connect('/about/terms-and-conditions',
                    controller='ckanext.openafrica.controller:CustomPageController',
                    action='toc')
        map.connect('/about/accessibility',
                    controller='ckanext.openafrica.controller:CustomPageController',
                    action='accessibility')
        map.connect('/about/code-of-conduct',
                    controller='ckanext.openafrica.controller:CustomPageController', 
                    action='coc')
        map.connect('/about/moderation-policy',
                    controller='ckanext.openafrica.controller:CustomPageController',
                    action='moderation')
        map.connect('/about/faq',
                    controller='ckanext.openafrica.controller:CustomPageController',
                    action='faq')
        map.connect('/about/privacy',
                    controller='ckanext.openafrica.controller:CustomPageController',
                    action='privacy')
        map.connect('/about/contact-us',
                    controller='ckanext.openafrica.controller:CustomPageController',
                    action='contact')
        map.connect('/about/suggest-a-dataset',
                    controller='ckanext.openafrica.controller:CustomPageController',
                    action='suggest_a_dataset')
        return map

    def get_helpers(self):
        """
        All functions, not starting with __ in the ckanext.openafrica.lib
        module will be loaded and made available as helpers to the
        templates.
        """
        from ckanext.openafrica.lib import helpers
        from inspect import getmembers, isfunction

        helper_dict = {}

        funcs = [o for o in getmembers(helpers, isfunction)]
        return dict([(f[0],f[1],) for f in funcs if not f[0].startswith('__')])
