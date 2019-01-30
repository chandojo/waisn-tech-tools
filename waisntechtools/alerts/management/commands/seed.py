from django.core.management import BaseCommand

from alerts.tests.fakes import SubscriberFactory


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
            SubscriberFactory.create()
