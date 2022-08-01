"""
ASGI config for gaint_plus project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import sys

path = '/home/figmavibes/gaint-plus'
if path not in sys.path:
    sys.path.insert(0,path)

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'gaint_plus.settings'

application = get_wsgi_application()
