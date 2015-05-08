# -*- coding: utf-8 -*-

from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
import local_settings as settings
import os


class NagiosDefaultLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("success")
    def onSuccess(self, successProtocolEntity):
        print("Succesfully connected to the WhatsApp service.")
        print(self.generateMessage())

    def getEmojiForState(self, state):
        emojis = {
            'None': '❓',
            'UNKNOWN': '❓',
            'CRITICAL': '🚨',
            'WARNING': '',
            'OK': '✅'
        }.get(state)

    def generateMessage(self):
        return "This is a py-nagios-wa test message."

    def __str__(self):
        return "Nagios Layer"


class NagiosServiceLayer(NagiosDefaultLayer):
    def generateMessage(self):
        notification = {
            'type': os.environ.get('NAGIOS_NOTIFICATIONTYPE'),
            'service': os.environ.get('NAGIOS_SERVICEDESC'),
            'host': os.environ.get('NAGIOS_HOSTALIAS'),
            'address': os.environ.get('NAGIOS_HOSTADDRESS'),
            'state': os.environ.get('NAGIOS_SERVICESTATE'),
            'emoji': self.getEmojiForState(os.environ.get('NAGIOS_SERVICESTATE')),
            'time': os.environ.get('NAGIOS_LONGDATETIME'),
            'info': os.environ.get('NAGIOS_SERVICEOUTPUT')
        }

        return settings.SERVICE_NOTIFICATION % notification


class NagiosHostLayer(NagiosDefaultLayer):
    def generateMessage(self):
        notification = {
            'type': os.environ.get('NAGIOS_NOTIFICATIONTYPE'),
            'host': os.environ.get('NAGIOS_HOSTALIAS'),
            'address': os.environ.get('NAGIOS_HOSTADDRESS'),
            'state': os.environ.get('NAGIOS_HOSTSTATE'),
            'emoji': self.getEmojiForState(os.environ.get('NAGIOS_HOSTSTATE')),
            'time': os.environ.get('NAGIOS_LONGDATETIME'),
            'info': os.environ.get('NAGIOS_HOSTOUTPUT')
        }

        return settings.HOST_NOTIFICATION % notification