from django.conf import settings
from django.http import HttpResponseForbidden

from twilio.rest import Client
from twilio.request_validator import RequestValidator

import requests

def fetch_twilio(request):
    validator = RequestValidator(TWILIO_AUTH_TOKEN)
    request_valid = validator.validate(
        request.build_absolute_uri(),
        request.POST,
        request.META.get('HTTP_X_TWILIO_SIGNATURE', ''))

    if request_valid:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_fetch = client.messages.list(to=TWILIO_SMS_NUMBER)
        return message_fetch
    else:
        return HttpResponseForbidden()
