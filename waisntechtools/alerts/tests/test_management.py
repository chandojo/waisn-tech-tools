from django.core.management import call_command
from django.core.management.commands import flush
from django.test import TestCase

from alerts.models import Subscriber


class SeedCommandTests(TestCase):
    def setUp(self):
        call_command(flush.Command(), interactive=False)

    def test_table_not_empty(self):
        num_users = 10
        call_command('seed', users=num_users)

        db_users = Subscriber.objects.all()
        self.assertEqual(num_users, len(db_users))

    def tearDown(self):
        call_command(flush.Command(), interactive=False)
