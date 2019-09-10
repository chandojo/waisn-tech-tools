import requests
from django.conf import settings
from twilio.rest import Client
from twilio.request_validator import RequestValidator

class Messenger(object):
    def __init__(self, client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)):
        self.client = client

    def send(self, subscriber, filenames):
        message_to = subscriber.phone_number
        for file in filenames:
            messageReply = Message(file)
            messageReply = messageReply.contents()
            message = self.client.messages.create(
                                          body=messageReply,
                                          from_=settings.TWILIO_SMS_NUMBER,
                                          to=message_to
                                      )

class Message(object):
    def __init__(self, file):
        self._file = file

    def contents(self):
        with open(self._file) as f:
            messageReply = f.read()
            return messageReply
