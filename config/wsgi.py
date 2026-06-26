import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.core.management import call_command

try:
    call_command("migrate", "--noinput")
    call_command("seed_data")
except Exception as e:
    print(f"Startup setup error: {e}", file=sys.stderr)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
