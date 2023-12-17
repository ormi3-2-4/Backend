"""
ASGI config for running_mate project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from running_mate.consumer import RunningMateWebSocket

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "running_mate.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(RunningMateWebSocket.as_asgi()),
    }
)
