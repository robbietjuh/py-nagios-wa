from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback


class NagiosDefaultLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("success")
    def onSuccess(self, successProtocolEntity):
        print("Succesfully connected to the WhatsApp service.")
        print(self.generateMessage())

    def generateMessage(self):
        return "This is a py-nagios-wa test message."

    def __str__(self):
        return "Nagios Layer"


class NagiosServiceLayer(NagiosDefaultLayer):
    def generateMessage(self):
        return "Service message"


class NagiosHostLayer(NagiosDefaultLayer):
    def generateMessage(self):
        return "Host message"