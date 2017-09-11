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
