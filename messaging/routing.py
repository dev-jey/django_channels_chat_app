from django.urls import re_path
from messaging.consumers import MessageConsumer

# URL for connecting users asynchronously to the server  to receive notifications
messaging_urlpatterns = [
    re_path(r'^ws/chat/(?P<username>[^/]+)/$$',
            MessageConsumer.as_asgi()),
]
