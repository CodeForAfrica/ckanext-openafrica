openAFRICA CKAN Extension
=========================

Website: [openAFRICA](http://openAFRICA.net)
Latest Version: 1.0.0

Currently on customises the look and feel in very basic ways.

Use http://docs.ckan.org/en/latest/contents.html to set up CKAN

Then follow the steps below to install the openAfrica extension:

Step 1:

* Activate your virtual environment; use the path to your virtual environment. On Mac OSX, you may have to use `/usr/local/lib/ckan/default/bin/activate`. You can copy the code as it is below, including the preceeding dot.
```
. /usr/lib/ckan/default/bin/activate
```

Step 2:

* Install the extension

If you are not a developer and just want to install the extension from package, just run this command from your virtual environment:
```
pip install ckanext-openafrica
```
> **Note**: If you wish to modify the extension in any way, you can download the source code and install the extension manually. To do so, execute the following command:
> ```
> $ pip install -e git+https://github.com/CodeForAfrica/ckanext-openafrica.git#egg=ckanext-openafrica
> ```
> **Alternatively**: You can clone this repo (preferrably into the /src directory where you installed CKAN), cd into ckanext-openafrica and run
> ```
> $ python setup.py develop
> ```

Step 3:

* Modify your configuration file (generally in `/etc/ckan/default/production.ini`) and add `openafrica` in the `ckan.plugins` property.
```
ckan.plugins = openafrica <OTHER_PLUGINS>
```

Step 4: 

* Restart your server:

```
paster serve /etc/ckan/default/production.ini
```
OR
```
paster serve --reload /etc/ckan/default/production.ini
```
With `--reload`, your server is restarted automatically whenever you make changes in your source code.

If your extension is installed successfully, your page will change to the openAfrica theme.

**Note**: This extension, being a thememing extension, may override templates from other extensions. Templates in /ckanext/openafrica/templates 
may require some modifications to render properly with openAfrica extension.

Support
-------
If you've found a bug/issue in the extension, open a new issue [here](https://github.com/CodeForAfrica/ckanext-openafrica/issues/new) _ (try
searching first to see if there's already an [issue](https://github.com/CodeForAfrica/ckanext-openafrica/issues) for your bug).



Contributing to ckanext-openafrica Extension
---------------------------------------------
If you have interest in contributing to the development of openAfrica extension, you are welcome. A good starting point
will be reading the CKAN general [Contributing guide](http://docs.ckan.org/en/ckan-2.7.0/contributing/index.html). Then you can checkout 
existing [issues](https://github.com/CodeForAfrica/ckanext-openafrica/issues) that are open for contribution; new features and issues are welcome.
To work on any issue, comment on the issue to indicate your interest and the issue will be assigned to you. It is always a good idea to seek
for clarification (where necessary) on any issue you work on.

**It is important that changes that require some form of configurations should be documented in the README.**

Copying and License
--------------------

This material is copyright (c) 2015-2017 Code for Africa.

It is open and licensed under the GNU Affero General Public License (AGPL) v2.0
whose full text may be found at:

http://www.gnu.org/licenses/gpl-2.0.html
