from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from generators import DefaultGenerator


class NagiosLayer(YowInterfaceLayer):
    generator = DefaultGenerator

    @ProtocolEntityCallback("success")
    def onSuccess(self, successProtocolEntity):
        print("Succesfully connected to the WhatsApp service.")

    def __str__(self):
        return "Nagios Layer"