.. TODO: Complete the README descriptions and "about" section.{% if False %}{# Hiding GitHub README #}

Django project template
=======================

This project template creates a Django 1.5 project with
a base set of applications

Features
---------

Installed apps:

* Django 1.5
* MySQLdb or Psycopg2
* Pillow (PIL replacement)
* SORL-Thumbnail_
* South_
* bpython_
* Raven_
* django-axes_
* django-admin-tools_
* django-compressor_
* django-crispy-forms_
* django-debugtools_
* django-filebrowser-no-grapelli_
* django-fluent-dashboard_
* django-google-analytics_

Configured URLs:

* ``/robots.txt``
* ``/sitemap.xml``
* ``/admin/``

Templates:

* ``base.html``
* ``404.html``
* ``500.html``

Features:

* Settings package
* WSGI deployment scripts
* CSS and JavaScript paths configured
* HTML5shiv + jQuery Installed
* Meyer-based CSS reset
* Working Compass_ + SASS_ + LiveReload_ setup (can be discarded)

Usage
-----

Create a Django project::

    mkdir my-website.com
    cd my-website.com
    django-admin.py startproject mywebsite . -e py,rst,example,gitignore --template=https://github.com/edoburu/django-project-template/archive/master.zip

Alternatively, you can place the files in a ``src`` folder too::

    mkdir -p my-website.com/src
    cd my-website.com
    django-admin.py startproject mywebsite src -e py,rst,example,gitignore --template=https://github.com/edoburu/django-project-template/archive/master.zip

This allows you to create folders like ``docs``, ``web``, ``logs``, ``etc`` at the toplevel.
This setup is recommended.

The remaining instructions - to start the development server - can be found in the generated ``README.rst`` file.


Django-fluent template
----------------------

In a second branch, you'll find a project template for the django-fluent_ CMS::

    mkdir my-website.com
    cd my-website.com
    django-admin.py startproject mywebsite . -e py,rst,example,gitignore --template=https://github.com/edoburu/django-project-template/archive/django-fluent.zip


Working with SCSS files
=======================

As extra treat, the CSS files are easier to edit using SASS_ and Compass_.

It gives these advantages to regular CSS:

* Variables.
* Nesting CSS selectors.
* Default mixins for CSS3 properties and vendor-prefixes.
* Typography features such as ellipses,
* Generating sprites, including ``background-position`` offsets.

.. note::

    This feature is optional. If you don't like to use it, the project already has a ``screen.css`` file which can be used and edited.
    Feel free to remove those files in your own projects or fork (``config.rb``, ``Guardfile``, and ``frontend/sass``).
    However, we highly recommended to take a look at it.

Using compass
-------------

Install Compass_ using::

    gem install compass bootstrap-sass oily_png

Leave Compass_ running in the terminal::

    compass watch

It automatically compiles the ``*.css`` files for you.


Using guard+livereload
----------------------

To make it even better, use guard-livereload_.
Now the browser can automatically refresh all styles inline.

Install guard-livereload_ using::

    gem install guard-livereload guard-compass

Leave it running in the terminal during development::

    guard

Install a browser plugin, see:

* Firefox (2.0.9 dev release): https://github.com/siasia/livereload-extensions/downloads
* Everyone else: http://help.livereload.com/kb/general-use/browser-extensions

And toggle the "LiveReload" button in the browser at the desired page.

Each time a change is made in ``*.scss`` files, the files are compiled and the browser reloads
the CSS file, even without reloading the entire page!

.. _bpython: http://bpython-interpreter.org/
.. _django-axes: https://github.com/django-security/django-axes
.. _django-admin-tools: https://bitbucket.org/izi/django-admin-tools
.. _django-compressor: http://django_compressor.readthedocs.org/
.. _django-crispy-forms: http://django-crispy-forms.readthedocs.org/
.. _django-debugtools: https://github.com/edoburu/django-debugtools
.. _django-filebrowser-no-grapelli: https://github.com/vdboor/django-filebrowser-no-grappelli-django14
.. _django-fluent-dashboard: https://github.com/edoburu/django-fluent-dashboard
.. _django-google-analytics: https://github.com/clintecker/django-google-analytics
.. _LiveReload: http://livereload.com/
.. _Raven: https://github.com/getsentry/raven-python
.. _SORL-Thumbnail: https://github.com/sorl/sorl-thumbnail
.. _South: http://south.readthedocs.org/


------------

.. {% else %}

{{ project_name|title }} Project
========================================

About
-----

Describe your project here.

Prerequisites
-------------

- Python >= 2.6
- pip
- virtualenv (virtualenvwrapper is recommended)

Installation
------------

To setup a local development environment::

    virtualenv env --prompt="({{ project_name }})"  # or mkvirtualenv {{ project_name }}
    source env/bin/activate

    pip install -r requirements.txt
    edit {{ project_name }}/settings/project.py    # Enter your DB credentials
    cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py  # To enable debugging

    ./manage.py syncdb --migrate
    ./manage.py runserver

Compiling CSS files
~~~~~~~~~~~~~~~~~~~

To compile SASS_ files::

    gem install compass bootstrap-sass oily_png guard-livereload guard-compass

    guard

To enable LiveReload_ of ``*.css`` files during development, install a browser plugin:

* Firefox (2.0.9 dev release): https://github.com/siasia/livereload-extensions/downloads
* Everyone else: http://help.livereload.com/kb/general-use/browser-extensions

And toggle the "LiveReload" button in the browser at the desired page.

License
-------

Describe project license here.


.. Add links here:{% endif %}

.. _Compass: http://compass-style.org/
.. _django-fluent: http://django-fluent.org/
.. _LiveReload: http://livereload.com/
.. _guard-livereload: https://github.com/guard/guard-livereload
.. _SASS: http://sass-lang.com/
