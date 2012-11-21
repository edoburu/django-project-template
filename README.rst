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

Usage
-----

Create a Django project::

    django-admin.py startproject -e py,example,gitignore --template=https://github.com/edoburu/django-project-template/archive/master.zip

