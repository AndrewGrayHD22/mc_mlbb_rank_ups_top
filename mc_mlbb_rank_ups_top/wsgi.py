"""
WSGI config for mc_mlbb_rank_ups_top project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mc_mlbb_rank_ups_top.settings")

application = get_wsgi_application()
