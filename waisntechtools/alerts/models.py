from django.db import models


# Subscribers have a subscription to receive text message alerts.
class Subscriber(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    language = models.CharField(max_length=3)
    subscription_state = models.CharField(max_length=20)
    date_registered = models.DateTimeField(max_length=20)

    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.date_registered,
            self.phone_number,
            self.language,
            self.subscription_state,
        )
