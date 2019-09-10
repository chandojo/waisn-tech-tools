from django.conf import settings
from django.http import HttpResponseForbidden
from twilio.rest import Client
from twilio.request_validator import RequestValidator

import requests
import datetime

def debug_twilio():
    messages=[]

    if settings.DEBUG == True:
        request_valid = True
    # TODO: create validator for production settings

    if request_valid:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        messages_list = client.messages.list(limit=10)

        for message in messages_list:
            messages.append(message)
        return messages
    else:
        return HttpResponseForbidden()
