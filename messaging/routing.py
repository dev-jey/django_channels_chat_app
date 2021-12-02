from django.urls import re_path
from messaging.consumers import MessageConsumer

# URL for connecting users asynchronously to the server  to receive notifications
messaging_urlpatterns = [
    re_path(r'^ws/chat/', MessageConsumer.as_asgi()),
    # Connect a user to this socket once they bid on an auction
    # re_path(r'^ws/notifications/outbid/(?P<username>[^/]+)/$$',
    #         OutbidNotificationConsumer.as_asgi()),
]
