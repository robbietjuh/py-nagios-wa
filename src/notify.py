#!/usr/bin/env python
from yowsup.layers.auth import YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.protocol_messages import YowMessagesProtocolLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.coder import YowCoderLayer
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS
from yowsup import env

from nagios import NagiosLayer


if __name__ == "__main__":
    # Import local settings
    try:
        import local_settings as settings
    except ImportError:
        print("Error: Could not import local settings. Exiting!")
        exit(1)

    # todo: Figure out which layer to use
    nagios_layer = NagiosLayer

    # Set up handler layers and credentials
    layers = (
                 nagios_layer,
                 (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer)
             ) + YOWSUP_CORE_LAYERS

    credentials = (settings.CREDENTIALS['username'], settings.CREDENTIALS['password'])

    # Set up Yowsup
    stack = YowStack(layers)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, credentials)
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())

    # Connect to WhatsApp
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    try:
        stack.loop()
    except AuthError as e:
        print("Authentication Error: %s" % e.message)