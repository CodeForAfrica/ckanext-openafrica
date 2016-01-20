import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class OpenAfricaPlugin(plugins.SingletonPlugin):
    '''OpenAfrica templating plugin done in 2015.

    '''
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
    
        toolkit.add_public_directory(config, 'public')
