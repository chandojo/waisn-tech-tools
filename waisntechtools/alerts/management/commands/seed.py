from django.core.management import BaseCommand
from django.utils import timezone
from factory import Faker
from factory.django import DjangoModelFactory
from faker.providers import BaseProvider
import random

from alerts.models import Subscriber


class Command(BaseCommand):
    help = 'Seeds the database with fake subscribers'
    _users_option = 'users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--{}'.format(Command._users_option),
            default=200,
            type=int,
            help='The number of fake users to create'
        )

    def handle(self, *args, **options):
        for _ in range(options[Command._users_option]):
            _SubscriberFactory.create()


class _SubscriberFactory(DjangoModelFactory):
    class Meta:
        model = Subscriber

    phone_number = Faker('phone_number')
    language = Faker('language')
    subscription_state = Faker('subscription_state')
    date_registered = Faker('date_time', tzinfo=timezone.get_current_timezone())


class _SubscriptionStateProvider(BaseProvider):
    _STATES = [
        'unsubscribed',
        'selecting_language',
        'complete',
    ]

    def __init__(self, generator):
        super().__init__(generator)
        self._rand = random.Random(42)

    def subscription_state(self):
        return _SubscriptionStateProvider._STATES[
            self._rand.randrange(0, len(_SubscriptionStateProvider._STATES))
        ]


class _LanguageProvider(BaseProvider):
    _LANGUAGES = [
        "eng",
        "spa",
        "kor",
        "cmn",
        "vie",
    ]

    def __init__(self, generator):
        super().__init__(generator)
        self._rand = random.Random(24)

    def language(self):
        return _LanguageProvider._LANGUAGES[
            self._rand.randrange(0, len(_LanguageProvider._LANGUAGES))
        ]


Faker.add_provider(_SubscriptionStateProvider)
Faker.add_provider(_LanguageProvider)
