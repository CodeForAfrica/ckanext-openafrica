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

u'''Defines openAFRICA plugin
Extends CKAN plugins core which provides plugin services to the CKAN
'''

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from . import blueprint


class OpenAfricaPlugin(plugins.SingletonPlugin):
    u"""
    openAFRICA templating plugin.
    """
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IBlueprint)

    def update_config(self, config):
        u"""
        Called by load_environment at earliest point when config is
        available to plugins. The config should be updated in place.

        :param config: ``config`` object
        """
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('assets', 'openafrica')

    # IBlueprint
    def get_blueprint(self):
        """
        CKAN uses Flask Blueprints to extend urls
        :return:
        """
        return blueprint.openafrica


    def get_helpers(self):
        u"""
        All functions, not starting with __ in the ckanext.openafrica.lib
        module will be loaded and made available as helpers to the
        templates.
        """
        from ckanext.openafrica.lib import helpers
        from inspect import getmembers, isfunction

        helper_dict = {}

        funcs = [o for o in getmembers(helpers, isfunction)]
        return dict([(f[0], f[1],) for f in funcs if not f[0].startswith('__')])
