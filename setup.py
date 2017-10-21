from setuptools import setup, find_packages

version = '0.9.1'

setup(
    name='ckanext-openafrica',
    version=version,
    description="CKAN extension for openAFRICA.",
    long_description="""\
    """,
    classifiers=[],
    keywords='ckan ckanext openafrica extension data theme',
    author='Code for Africa',
    author_email='support@codeforafrica.org',
    url='http://openafrica.net',
    license='GPL v2.',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.openafrica'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    # Add plugins here, eg
    # myplugin=ckanext.openafrica:PluginClass
    openafrica=ckanext.openafrica.plugin:OpenAfricaPlugin
    """,
)
