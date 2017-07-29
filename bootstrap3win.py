import os
import subprocess

run = subprocess.getstatusoutput

status, output = run('virtualenv .env')
print(output)

status, output = run('.env/Scripts/pip.exe install --upgrade setuptools')
print(output)

status, output = run('.env/Scripts/pip.exe install --upgrade pip')
print(output)

status, output = run('.env/Scripts/pip.exe install zc.buildout')
print(output)

TPL = """
[buildout]
parts = base wwcw7 wsgi
unzip = true
newest = false
versions = versions

[versions]
mk.recipe.pip = 0.3

[base]
recipe = zc.recipe.egg
find-links =
    http://django-template-utils.googlecode.com/files/template_utils-0.4p2.tar.gz
    https://github.com/k4ml/mk.recipe.modwsgi/archive/master.zip#egg=mk.recipe.modwsgi
eggs = 
    MySQL-python
    Django
    django-storages
    template-utils
    django-allauth
    django-widget-tweaks
    requests
    Jinja2
scripts =

[wwcw7]
project-name = wwcw7
recipe = zc.recipe.egg
eggs =
    ${base:eggs}
interpreter = python
extra-paths = ${buildout:directory}/src
settings = wwcw7.settings
entry-points =
    manage=django.core.management:execute_from_command_line
initialization =
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = '${:settings}'
scripts =
    manage
    python

[wsgi]
recipe = mk.recipe.modwsgi
settings = ${wwcw7:settings}
eggs = ${wwcw7:eggs}
extra-paths = ${wwcw7:extra-paths}
makedir = true
wsgi-module = wwcw7.wsgi
target = ${buildout:directory}/parts/wsgi/www.wsgi
initialization =
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = '${:settings}'
"""

f = open('buildout.cfg', 'w')
f.write(TPL)

status, output = run('.env/Scripts/buildout.exe bootstrap')
print(output)
