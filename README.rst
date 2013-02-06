Django project template
=======================

This project template creates a Django 1.4 project with
a base set of applications

Features
---------

Installed apps:

* Django 1.4
* MySQLdb
* Pillow (PIL replacement)
* SORL Thumbnail
* South
* bpython
* django-admin-tools
* django-compressor
* django-crispy-forms
* django-debugtools
* django-filebrowser-no-grapelli
* django-fluent-dashboard
* django-google-analytics

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
    django-admin.py startproject mywebsite . -e py,example,gitignore --template=https://github.com/edoburu/django-project-template/archive/master.zip

Alternatively, you can place the files in a ``src`` folder too::

    mkdir -p my-website.com/src
    cd my-website.com
    django-admin.py startproject mywebsite src -e py,example,gitignore --template=https://github.com/edoburu/django-project-template/archive/master.zip

This allows you to create folders like ``docs``, ``web``, ``logs``, ``etc`` at the toplevel.
This setup is recommended.


Working with SCSS files (optional!)
===================================

As extra present, the CSS files are easier to edit using SASS_ and Compass_.

It gives these advantages to regular CSS:

* Variables.
* Nesting CSS selectors.
* Default mixins for CSS3 properties and vendor-prefixes.
* Typography features such as ellipses,
* Generating sprites, including ``background-position`` offsets.

.. note::

    This feature is optional! The project already has a ``screen.css`` file which can be used and edited.
    Feel free to remove those files in your own projects or fork (``config.rb``, ``Guardfile``, and ``frontend/sass``).


Using compass
-------------

Install Compass_ using::

    gem install compass bootstrap-sass oily_png

Leave Compass_ running in the terminal::

    compass watch --poll

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


.. _Compass: http://compass-style.org/
.. _SASS: http://sass-lang.com/
.. _LiveReload: http://livereload.com/
.. _Guard: https://github.com/guard/guard
.. _guard-livereload: https://github.com/guard/guard-livereload
