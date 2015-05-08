# -*- coding: utf-8 -*-
import threading

from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import local_settings as settings
import os


class NagiosDefaultLayer(YowInterfaceLayer):
    def __init__(self):
        super(NagiosDefaultLayer, self).__init__()
        self.queue = []
        self.lock = threading.Condition()

    @ProtocolEntityCallback("success")
    def onSuccess(self, successProtocolEntity):
        self.lock.acquire()

        print("Succesfully connected to the WhatsApp service.")

        for recipient in settings.DEFAULT_RECIPIENTS:
            print("Sending to " + recipient)
            messageEntity = TextMessageProtocolEntity(self.generateNotificationText(), to=recipient)
            self.queue.append(messageEntity.getId())
            self.toLower(messageEntity)

        self.lock.release()

    @ProtocolEntityCallback("ack")
    def onAck(self, entity):
        self.lock.acquire()

        if entity.getId() in self.queue:
            self.queue.remove(entity.getId())

        if len(self.queue) == 0:
            print("All messages have been sent. Disconnecting now!")
            self.disconnect()

        self.lock.release()

    def getEmojiForState(self, state):
        emojis = {
            'None': '❓',
            'UNKNOWN': '❓',
            'CRITICAL': '🚨',
            'WARNING': '',
            'OK': '✅'
        }

        return emojis.get(state)

    def generateNotificationText(self):
        return " ".join((self.getEmojiForState('OK'), "This is a py-nagios-wa test message.",))

    def __str__(self):
        return "Nagios Layer"


class NagiosServiceLayer(NagiosDefaultLayer):
    def generateNotificationText(self):
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
    def generateNotificationText(self):
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