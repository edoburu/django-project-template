.. TODO: Complete the README descriptions and "about" section.{% if False %}{# Hiding GitHub README #}

.. image:: https://img.shields.io/travis/edoburu/django-project-template/master.svg?branch=master
    :target: http://travis-ci.org/edoburu/django-project-template
.. image:: https://img.shields.io/codecov/c/github/edoburu/django-project-template/master.svg
    :target: https://codecov.io/github/edoburu/django-project-template?branch=master

Django project template
=======================

This project template creates a Django 1.8 / 1.9 project with
a base set of applications

Features
---------

Installed apps:

* Django 1.8+
* MySQLdb or Psycopg2
* py.test_ and coverage setup
* Pillow_
* SORL-Thumbnail_
* IPython_ + ptpython_
* Raven_
* django-analytical_
* django-axes_
* django-admin-tools_
* django-compressor_
* django-crispy-forms_
* django-debugtools_
* django-filebrowser-no-grapelli_
* django-fluent-dashboard_
* django-ping_

Configured URLs:

* ``/robots.txt``
* ``/sitemap.xml``
* ``/admin/``

Templates:

* ``base.html``
* ``403.html``
* ``404.html``
* ``500.html``

Features:

* Settings package
* WSGI deployment scripts
* CSS and JavaScript paths configured
* HTML5shiv + jQuery Installed
* Bootstrap 3 based CSS reset
* Gulpfile with SASS_, LiveReload_ and spritesmith_ setup (can be discarded)
* Uptime monitoring URL (``/api/ping/``)

Usage
-----

Create a Django project:

.. code-block:: bash

    mkdir my-website.com
    cd my-website.com
    django-admin.py startproject mywebsite . -e py,rst,example,gitignore,ini --template=https://github.com/edoburu/django-project-template/archive/master.zip

Alternatively, you can place the files in a ``src`` folder too:

.. code-block:: bash

    mkdir -p my-website.com/src
    cd my-website.com
    django-admin.py startproject mywebsite src -e py,rst,example,gitignore,ini --template=https://github.com/edoburu/django-project-template/archive/master.zip

This allows you to create folders like ``docs``, ``web``, ``logs``, ``etc`` at the toplevel.
This setup is recommended.

The remaining instructions - to start the development server - can be found in the generated ``README.rst`` file.


Django-fluent template
----------------------

In a second branch, you'll find a project template for the django-fluent_ CMS:

.. code-block:: bash

    mkdir my-website.com
    cd my-website.com
    django-admin.py startproject mywebsite . -e py,rst,example,gitignore,ini --template=https://github.com/edoburu/django-project-template/archive/django-fluent.zip


Optional features
=================

As extra treat, the CSS files are easier to edit using SASS_.
Changes are automatically visible in the browser using LiveReload_.

.. note::

    This feature is optional. If you don't like to use it, the project already has a ``screen.css`` file which can be used and edited.
    Feel free to remove those files in your own projects or fork (``gulpfile.js``, ``package.json``, and ``frontend/sass``).
    However, we highly recommended to take a look at it.

.. _bpython: http://bpython-interpreter.org/
.. _django-analytical: https://github.com/jcassee/django-analytical
.. _django-axes: https://github.com/django-security/django-axes
.. _django-admin-tools: https://bitbucket.org/izi/django-admin-tools
.. _django-compressor: https://django_compressor.readthedocs.io/
.. _django-crispy-forms: https://django-crispy-forms.readthedocs.io/
.. _django-debugtools: https://github.com/edoburu/django-debugtools
.. _django-filebrowser-no-grapelli: https://github.com/vdboor/django-filebrowser-no-grappelli-django14
.. _django-fluent-dashboard: https://github.com/edoburu/django-fluent-dashboard
.. _django-ping: https://github.com/rizumu/django-ping
.. _LiveReload: http://livereload.com/
.. _IPython: http://ipython.org/
.. _Pillow: https://github.com/python-pillow/Pillow
.. _ptpython: https://github.com/jonathanslenders/ptpython
.. _py.test: http://docs.pytest.org/
.. _Raven: https://github.com/getsentry/raven-python
.. _SORL-Thumbnail: https://github.com/sorl/sorl-thumbnail
.. _spritesmith: https://github.com/twolfson/gulp.spritesmith


------------

.. {% else %}

{{ project_name|title }} Project
========================================

About
-----

Describe your project here.

Prerequisites
-------------

- Python >= 2.7
- pip
- virtualenv (virtualenvwrapper is recommended)

Installation
------------

To setup a local development environment::

    virtualenv env --prompt="({{ project_name }})"  # or mkvirtualenv {{ project_name }}
    source env/bin/activate

    pip install -r dev-requirements.txt
    edit {{ project_name }}/settings/project.py    # Enter your DB credentials
    cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py  # To enable debugging

    sudo su - postgres
    createuser {{ project_name }}  -P   # testtest is the default password
    createdb --template=template0 --encoding='UTF-8' --lc-collate='en_US.UTF-8' --lc-ctype='en_US.UTF-8' --owner={{ project_name }} {{ project_name }}
    exit

    ./manage.py migrate
    ./manage.py runserver

Compiling SASS files
~~~~~~~~~~~~~~~~~~~~

Sass files are compiled to CSS during the development.
At the server, there is no need for installing development tools.

To setup your development system, install NodeJS from https://nodejs.org/.
On Mac OSX, you can also use ``brew install libsass node``.

Run the following command to compile SASS_ files::

    npm run gulp

This will compile the files, and watch for changes.
It also has LiveReload_ support.
Install a browser plugin from: http://livereload.com/extensions/
and toggle the "LiveReload" button in the browser to see CSS changes instantly.

License
-------

Describe project license here.


.. Add links here:{% endif %}

.. _django-fluent: http://django-fluent.org/
.. _LiveReload: http://livereload.com/
.. _SASS: http://sass-lang.com/
